import urllib
import requests
import json
from bs4 import BeautifulSoup

home_page = 'https://www.statbunker.com/'
initial_page = 'https://www.statbunker.com'
initial_link = urllib.urlopen(home_page).read()
soup = BeautifulSoup(initial_link, "lxml")
tournaments_html = soup.find("div", id="mainContent").find_all("a")

'''
Construct Tournaments dictionary
of Tournament name, Link to Tournament
'''
tournaments = {}
for tournament in tournaments_html:
	tournaments[tournament.get_text()] = {}
	tournaments[tournament.get_text()]["link"] = home_page + tournament.get('href')
	temp_link = urllib.urlopen(tournaments[tournament.get_text()]["link"]).read()
	temp_soup = BeautifulSoup(temp_link, "lxml")
	teams_html = temp_soup.find("div", id="mainContent").find("table").find_all("tr")
	for team in teams_html:
		link = team.find("a")
		if(link is not None):
			tournaments[tournament.get_text()][link.get_text()] = {}
			tournaments[tournament.get_text()][link.get_text()]["team_name"] = link.get_text()
			tournaments[tournament.get_text()][link.get_text()]["link"] = initial_page + link.get('href')

#print(tournaments)
with open("tournaments.json", "w") as writeJSON:
    json.dump(tournaments, writeJSON, sort_keys=True, indent=4, separators=(',', ': '))

