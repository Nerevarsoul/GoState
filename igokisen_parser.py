from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

_base_url = "http://igokisen.web.fc2.com/news.html"
_site_url = "http://igokisen.web.fc2.com/"


def _get_urls():
    doc = BeautifulSoup(requests.get(_base_url).content)
    trs = doc.find("tr", class="center back5")
    for tr in trs:
        tds = tr.find_all('td')
        tour = td[0].find_all("a")[0]
        href = urljoin(_site_url, tour["href"])
        name = tour["text"]
        update = td[-1]["text"]
