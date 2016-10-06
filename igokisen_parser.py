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
    conn = connect_to_database()
    if conn:
       cur = conn.cursor() 
       for entry in _get_urls():
            cur.execute("INSERT INTO title (name, holding, country, current_winner, status) VALUES (%s, %s, %s, %s, 'active')", (entry['titleName'], entry['holding'], entry['countryName'], entry['winnerName']))
       conn.commit()
       cur.close()
       conn.close()
    

if __name__ == '__main__':
    main()

