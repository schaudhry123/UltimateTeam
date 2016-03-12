import urllib
import json
import pymongo
from bs4 import BeautifulSoup

home_page = 'http://www.whoscored.com'
initial_link = urllib.urlopen('http://www.whoscored.com').read()
soup = BeautifulSoup(initial_link, "lxml")
tournaments_html = soup.find("ul", id="popular-tournaments-list")

'''
Construct Tournaments dictionary
of Tournament name, Link to Tournament
'''
tournaments = {}
for tournament in tournaments_html:
	for links in tournament.find_all('a'):
		tournaments[links.get_text()] = {}
		tournaments[links.get_text()]["link"] = home_page + links.get('href')

print(tournaments)
with open("tournaments.json", "w") as writeJSON:
    json.dump(tournaments, writeJSON, sort_keys=True, indent=4, separators=(',', ': '))

