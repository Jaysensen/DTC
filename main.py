from bs4 import BeautifulSoup
from functions import printRankings
from functions import runTradeCalculator
from player import Player
import requests

# getting data from keeptradecut
html_text = requests.get('https://keeptradecut.com/dynasty-rankings').text
soup = BeautifulSoup(html_text, 'lxml')



PlayersList = []
# finding the players on the rankings webpage
players = soup.find_all('div', class_ = 'onePlayer')
for player in players:

    # getting first and last name of the player
    firstname = player.find('p', class_ = 'player-name').text.split()[-2]
    lastname = player.find('p', class_ = 'player-name').text.split()[-1]
    name = firstname + ' ' + lastname

    # getting the team the player plays for
    team = player.find('span', class_ = 'player-team').text

    # getting the players rank with respect to the others in the same position
    rank = player.find('p', class_ = 'position').text

    # using the rank to get the position
    position = rank[0] + rank[1]

    # getting the age of the player    
    if rank != "PICK":
        age = player.find('div', class_ = 'position-team').text.split()[1]

    # removing the first character from the age string because of weird formatting on KTC
    age = age[1:]
    age = age + " y.o"
    # getting the players current value on the trade market according to keeptradecut
    value = player.find('div', class_ = 'value').text.strip()
    
    # creating a new player object with the values we pulled from the site
    newPlayer = Player(name, team, position, rank, value, age)

    # adding the new player to our players list
    PlayersList.append(newPlayer)
    

print("-----------------Welcome to Jaysen's Dynasty Trade Calculator Program!-----------------")
while(1):
    
    print("Please enter a number corresponding to the function you would like to use\n")
    userI = input("1. Trade Calculator \n2. Rankings\n")
    print("You entered: " + userI) 
    if userI == '':
        print("Invalid input")
        continue
    elif int(userI) == 1:
        print("Inside if 1")
        runTradeCalculator(PlayersList)
    elif int(userI) == 2:
        print("Inside if 2")
        printRankings(PlayersList)
    
    else:
        print("Invalid input")
        
    




