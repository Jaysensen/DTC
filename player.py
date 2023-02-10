playersList = []
class Player:


    def __init__(self, name, team, position, rank, value, age):
        self.name = name
        self.team = team
        self.position = position
        self.rank = rank
        self.value = value
        self.age = age

    

    def printPlayer(self):
        if self.position == "PI":
            print("Name:", self.name, "|", "Team:", "N/A", "|", "Position:", self.position, "|", "Rank:", self.rank, "|", "Value:", self.value, "|", "Age:", "N/A", "\n")
        else:
            print("Name:", self.name, "|", "Team:", self.team, "|", "Position:", self.position, "|", "Rank:", self.rank, "|", "Value:", self.value, "|", "Age:", self.age, "\n")

    

    

