import json
from datetime import datetime
from urlparse import urljoin

import requests
from bs4 import BeautifulSoup

from web.models import Player, Title, Tournament, Game
from web.server import db


_igokisen_news_url = "https://k2ss.info/igo/news.json"
_igokisen_site_url = "https://k2ss.info/igo"


def get_or_create_igokisen_player(name, country_name):
    if not name or 'Team' in name:
        return
    last_name = name.split()[0]
    first_name = name.split()[1].split('(')[0]
    player = Player.query.filter_by(last_name=last_name, first_name=first_name).first()
    if player:
        return player
    player = Player.query.filter_by(last_name=first_name, first_name=last_name).first()
    if player:
        return player
    rank = name.split()[1].split('(')[1]
    if not rank.isdigit():
        rank = None
    player = Player(last_name=last_name, first_name=first_name, rank=rank, country=country_name)
    return player


def get_or_create_tournament(title_id, player_id, holding):
    tour = Tournament.query(title=title_id, holding=holding).first()
    if tour:
        if not tour.winner and player_id:
            tour.winner = player_id
    else:
        tour = Tournament(title=title_id, holding=holding, winner=player_id)
    db.session.add(tour)
    db.session.commit()
    return tour


def update_title(json_title):
    title = Title.query.filter_by(name=json_title['titleName'], country=json_title['countryName']).first()
    player = get_or_create_igokisen_player(json_title['winnerName'], json_title['countryName'])

    if not title:
        title = Title(name=json_title['titleName'], country=json_title['countryName'])
        title.igo_url = urljoin(json_title['countryNameAbbreviation'], json_title['htmlFileName'])
    title.holding = json_title['holding']
    if player:
        title.current_winner = player.id
    title.time_edited = datetime.now()
    
    db.session.add(title)
    db.session.commit()

    if not Tournament.query.filter_by(title=title.id, holding=title.holding):
        get_or_create_tournament(title.id, player.id, json_title)


def igokisen_get_json():
    data = requests.get(_igokisen_base_url).content
    json_data = json.loads(data.decode())    
    return json_data


def get_games(title):
    url = 'http://igokisen.web.fc2.com/wr/ig.html'
    # url = title.igo_url
    data = requests.get(url).content
    soup = BeautifulSoup(data, 'html.parser')
    title_tables = soup.find_all('h2', class_='left')

    for title_table in title_tables:
        table = title_table.find_next_sibling('br').find('table')
        game_hrefs = [game.get('href') for game in table.find_all('a')]
        games = Game.query.filter_by(igo_url__in=game_hrefs).with_entities('igo_url').all()

        for href in game_hrefs:
            if href not in games:
                game_url = urljoin(_igokisen_site_url, '/wr', href)
                game_data = requests.get(game_url).content
                game_strings = game_data.decode('utf-8').split('\n')
                for row in game_strings:
                    if row.startswith('EV'):
                        event = row[3: -1]
                        holding = event.split(title.name)[0]
                        continue
                    if row.startswith('PW'):
                        white_player = get_or_create_igokisen_player(row[3: -1], title.country)
                        continue
                    if row.startswith('PB'):
                        black_player = get_or_create_igokisen_player(row[3: -1], title.country)
                        continue
                    if row.startswith('DT'):
                        game_date = row[3: -1]
                        continue
                    if row.startswith('RE'):
                        result = row[3: -1]
                        continue
                    if row.startswith(';B'):
                        break
                game = Game(white_player=white_player, black_player=black_player, date=game_date, result=result)
                game.tournament = get_or_create_tournament(title, None, holding)
        return


def get_gokifu_game_data(game_data):
    fields = {'black_player': ']PB[', 'white_player': ']PW[', 'event': ']EV[', 'date': ']DT[', 'result': ']RE['}
    for field in fields:
        index = game_data.index(fields[field])
        if index:
            fields[field] = ''
            while game_data[index+4] != ']':
                fields[field] += game_data[index+4]
                index += 1
    return fields

