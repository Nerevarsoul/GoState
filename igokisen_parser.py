import psycopg2
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

from secret import *

_base_url = "http://igokisen.web.fc2.com/news.html"
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
    doc = BeautifulSoup(requests.get(_base_url).content, "html.parser")
    trs = doc.find_all("tr", _class="back5")
    for tr in trs:
        tds = tr.find_all('td')
        tour = td[0].find_all("a")[0]
        href = urljoin(_site_url, tour["href"])
        name = tour["text"]
        update = td[-1]["text"]
        names.append(name)
    return names


def main():
    names = _get_urls()
    for name in names:
        print(name)
    

if __name__ == '__main__':
    main()

