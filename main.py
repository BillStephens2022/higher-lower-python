from art import logo, vs
from game_data import data
import random

def pick_random():
    pick_1 = random.choice(data)
    pick_2 = random.choice(data)
    if pick_1 == pick_2:
        while pick_1 == pick_2:
            pick_2 = random.choice(data)
    print(f"Compare A: {pick_1['name']}, a {pick_1['description']}, from {pick_1['country']}")
    print(vs)
    print(f"Compare B: {pick_2['name']}, a {pick_2['description']}, from {pick_2['country']}")
    if pick_1['follower_count'] > pick_2['follower_count']:
        result = 'A'
    else:
        result = 'B'
    
    return result

def check_choice(user_choice, answer):
    if user_choice == answer:
        return "you are right"
    else:
        return "you are wrong"



print(logo)
answer = pick_random()
user_choice = (input("Who has more followers?  Type 'A' or 'B': ")).upper()
print(user_choice)
print(check_choice(user_choice, answer))
