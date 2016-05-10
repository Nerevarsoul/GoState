from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup


_base_url = "https://en.wikipedia.org/wiki/List_of_professional_Go_tournaments"
_site_url = "https://en.wikipedia.org/"

def _get_urls():
    doc = BeautifulSoup(requests.get(_base_url).content)
    japan = doc.find("span", id="Japan").parent
    japan_major = japan.find_next("ul")
    for li in japan_major.find_all("li"):
        href = urljoin(_site_url, li.find_all("a")[0]["href"])
        yield href
        
        
def _get_data(url):
    doc = BeautifulSoup(requests.get(url).content)
    winners = doc.find("span", id="Past_winners").parent
    table_winners = winners.find_next("table", class_="wikitable")
    for tr in table_winners.find_all("tr")[1:]:
        td = tr.find_all("td")
        year = td[0].get_text()
        winner = td[1].get_text()
        score = td[2].get_text()
        runner-up = td[3].get_text()
        yield {'year': year, 'winner': winner, 'score': score, 'runner-up': runner-up}
