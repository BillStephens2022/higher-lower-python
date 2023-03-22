from art import logo, vs
from game_data import data
import random

def pick_random():
    pick_1 = random.choice(data)
    pick_2 = random.choice(data)
    if pick_1 == pick_2:
        while pick_1 == pick_2:
            pick_2 = random.choice(data)
    print(pick_1)
    print(pick_2)

print(logo)
print(vs)
pick_random()
