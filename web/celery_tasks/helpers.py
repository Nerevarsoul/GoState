import json
import requests
from datetime import datetime

from server.models import Title


_igokisen_base_url = "http://igokisen.web.fc2.com/news.json"
_igokisen_site_url = "http://igokisen.web.fc2.com/"


def update_title(json_title):
    title = Title.query.filter_by(name=json_title.titleName)
    title.holding = json_title.holding
    title.current_winner = json_title.winnerName
    title.time_edited = datetime.now()
    title.save()


def igokisen_get_json():
    data = requests.get(_igokisen_base_url).content
    json_data = json.loads(data.decode())    
    return json_data

