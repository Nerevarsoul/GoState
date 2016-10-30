import requests

from .server import celery


_igokisen_base_url = "http://igokisen.web.fc2.com/news.json"
_igokisen_site_url = "http://igokisen.web.fc2.com/"


@celery.task
def update_igokisen():
    titles = _igokisen_get_json()
    return


def _igokisen_get_json():
    data = requests.get(_igokisen_base_url).content
    json_data = json.loads(data.decode())    
    return json_data

