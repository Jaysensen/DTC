
def printRankings(PlayersList):

        for i in range(len(PlayersList)):
            PlayersList[i].printPlayer()

def runTradeCalculator(PlayersList):
    teamA = [], teamB = []
    teamASum, teamBSum = 0
    userInput = 1
    userinput = print("Enter players for team A\n Enter 0 when finished with team A")
    while userinput != 0:
        for player in PlayersList:
            if player.name == userInput:
                teamA.append()
                break
            
    userInput = 1
    userinput = print("Enter players for team B\n Enter 0 when finished with team B")   
    while userinput != 0:
        for player in PlayersList:
            if player.name == userInput:
                teamB.append()
                break

    print("Calculating...")
    for player in teamA:
        teamASum += player.value

    for player in teamB:
        teamBSum += player.value
    
    if teamASum >= teamBSum:
        print("Favors teamA")
    else:
        print("Favors teamB")
