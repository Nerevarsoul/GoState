import json
import requests
from datetime import datetime

from web.models import Player, Title
from web.server import db


_igokisen_base_url = "http://igokisen.web.fc2.com/news.json"
_igokisen_site_url = "http://igokisen.web.fc2.com/"


def get_or_create_igokisen_player(winner_name, country_name):
    if 'Team' in winner_name:
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


def update_title(json_title):
    title = Title.query.filter_by(name=json_title['titleName'], country=json_title['countryName']).first()
    if title:
        title.holding = json_title['holding']
        title.current_winner = json_title['winnerName']
        title.time_edited = datetime.now()
    else:
        title=Title(name=json_title['titleName'], country=json_title['countryName'],
                    holding=json_title['holding'], current_winner=json_title['winnerName'])
    db.session.add(title)
    db.session.commit()


def igokisen_get_json():
    data = requests.get(_igokisen_base_url).content
    json_data = json.loads(data.decode())    
    return json_data

