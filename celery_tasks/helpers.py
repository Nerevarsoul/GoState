import json
import requests
from datetime import datetime

from web.models import Player, Title, Tournament
from web.server import db


_igokisen_base_url = "http://igokisen.web.fc2.com/news.json"
_igokisen_site_url = "http://igokisen.web.fc2.com/"


def get_or_create_igokisen_player(winner_name, country_name):
    if not winner_name or 'Team' in winner_name:
        return
    last_name = winner_name.split()[0]
    first_name = winner_name.split()[1].split('(')[0]
    player = Player.query.filter_by(last_name=last_name, first_name=first_name).first()
    if player:
        return player
    rank = winner_name.split()[1].split('(')[1]
    if not rank.isdigit():
        rank = None
    player = Player(last_name=last_name, first_name=first_name, rank=rank, country=country_name)
    return player


def create_tournament(title_id, player_id, holding):
    tour = Tournament(title=title_id, holding=holding, winner=player_id)
    db.session.add(tour)
    db.session.commit()


def update_title(json_title):
    title = Title.query.filter_by(name=json_title['titleName'], country=json_title['countryName']).first()
    player = get_or_create_igokisen_player(json_title['winnerName'], json_title['countryName'])

    if not title:
        title=Title(name=json_title['titleName'], country=json_title['countryName'])
    title.holding = json_title['holding']
    if player:
        title.current_winner = player.id
    title.time_edited = datetime.now()
    
    db.session.add(title)
    db.session.commit()

    if not Tournament.query.filter_by(title=title.id, holding=title.holding):
        create_tournament(title.id, player.id, json_title)



def igokisen_get_json():
    data = requests.get(_igokisen_base_url).content
    json_data = json.loads(data.decode())    
    return json_data

