import json
import psycopg2
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

from secret import *

_base_url = "http://igokisen.web.fc2.com/news.json"
_site_url = "http://igokisen.web.fc2.com/"


def connect_to_database():
    try:
        conn=psycopg2.connect("dbname='gostate' user='gostate_user' password='{}'".format(DATABASE_PASS))
    except:
        print("I am unable to connect to the database.")
        conn = False
    return conn


def _get_urls():
    names = []
    data = requests.get(_base_url).content
    json_data = json.loads(data.decode())    
    return json_data


def main():
    json_data = _get_urls()
    for entry in json_data:
        print(entry['titleName'])
    

if __name__ == '__main__':
    main()

