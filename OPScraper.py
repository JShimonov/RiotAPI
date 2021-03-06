import requests
from bs4 import BeautifulSoup

name = input('in-game name: ')
URL = 'https://na.op.gg/summoner/userName=' + name
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(class_='MostChampionContent')

champs = results.find_all('div', class_='ChampionBox Ranked')
print(type(champs))

for i in range(5):
    champ = champs[i]
    champion = champ.find('div', class_='ChampionName').text.strip()
    kda = champ.find('span', class_='KDA').text.strip()
    played = champ.find('div', class_='Played')

    win_ratio = played.find('div', title='Win Ratio').text.strip()
    totalPlayed = played.find('div', class_='Title').text.strip()

    print("Champion: " + champion)
    print("Your KDA for " + champion + " is " + kda)
    print("Your win ratio for " + champion + " is " + win_ratio)
    print(str(totalPlayed).lower() + " games on " + champion)
    print()

# print(champs)
