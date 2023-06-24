"""
Basically, we perform operations on data structure while creating these. In one line
"""
import math

# Here we are multiplying by 2 in each element of list.

ans = [int(x) * 2 for x in input().strip().split(" ")]
print(ans)

"""
Find square root of elements in list
"""

ans1 = [math.sqrt(int(x)) for x in input().strip().split(" ")]
print(ans1)

ans3 = [x for x in input().strip().split(" ") if int(x) % 2 == 0]  # Print only even elements
print(ans3)

# ---- SET comprehension ----------------------

ans4 = {x for x in input().strip().split(" ")}  # basically an unordered set
print(ans4)

# ---- Dictionary -----
dictionary = {"John": 1, "Wick": 2, "Jason": 3, "Stephen": 4}
ans = {key: value for key, value in dictionary.items() if value > 2}
print(type(ans), ans)

"""
Given a list of players, find all players who have score more than 50 goals in Champions League and do not 
represent European nations.
"""

players = [
    {
        "name": "Lionel Messi",
        "country": "Argentina",
        "continent": "America",
        "goals": 100
    },
    {
        "name": "Thomas Muller",
        "country": "Germany",
        "continent": "Europe",
        "goals": 51
    },
    {
        "name": "Luis Suarez",
        "country": "Uruguay",
        "continent": "America",
        "goals": 60
    },
    {
        "name": "Christiano Ronaldo",
        "country": "Portugal",
        "continent": "Europe",
        "goals": 120
    },
    {
        "name": "Emi Martinez",
        "country": "Argentina",
        "continent": "America",
        "goals": 40
    }
]
non_european_players = [player for player in players if player["continent"] != "Europe" and player["goals"] >= 50]
print(non_european_players)
