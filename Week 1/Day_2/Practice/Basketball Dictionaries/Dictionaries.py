# class for player
#Update the constructor to accept a dictionary (player) as an argument and set the attributes using the dictionary
class Player:
    def __init__(self, name, age, position, team):
        # using dictionary to set attributes
        self.name = name
        self.age = age
        self.position = position
        self.team = team

# method to display player information 
    def display_info(self):
        print(f"Name: {self.name}, Age; {self.age}, Position: {self.position}, Team: {self.team}")
        return self
# some example dictionaries to show some players
# 2: Create 3 instances of the Player class using the given dictionaries
kevin = {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
}
jason = {
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
}
kyrie = {
    "name": "Kyrie Irving", 
    "age":32,
    "position": "Point Guard", 
    "team": "Brooklyn Nets"
}
#  creation instances 
Player.kevin = Player(kevin["name"], kevin["age"], kevin["position"], kevin["team"])
Player.Jason = Player(jason["name"], jason["age"], jason["position"], jason["team"])
Player.Kyrie = Player(kyrie["name"], kyrie["age"], kyrie["position"], kyrie["team"])

# display information for each player 
Player.kevin.display_info()
Player.Jason.display_info()
Player.Kyrie.display_info()

# example list of player dictionaries
# challenge 3 Populate a new list with Player instances from the list of players.
Players = [
    {"name": "Kevin Durant", "age":34, "position": "small forward", "team": "Brooklyn Nets"},
    {"name": "Jason Tatum", "age":24, "position": "small forward", "team": "Boston Celtics"},
    {"name": "Kyrie Irving", "age":32, "position": "Point Guard", "team": "Brooklyn Nets"},
    {"name": "Damian Lillard", "age":33, "position": "Power Forward", "team": "Portland Trailblazers"},
    {"name": "Joel Embiid", "age":32, "position": "Power Forward", "team": "Philadelphia 76ers"},
    {"name": "DeMar DeRozan", "age":32, "position": "Shooting Guard", "team": "Chicago Bulls"},
]
# empty placee to hold player instance 
new_team = []
# loop to create player instances and populate the list
for player_data in Players:
    new_team.append(Player(player_data["name"], player_data["age"], player_data["position"], player_data["team"]))

# display information for each player in new_team 
for player in new_team:
    player.display_info()