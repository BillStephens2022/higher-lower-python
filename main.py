from art import logo, vs
from game_data import data
import random

score = 0
game_over = False

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

def check_choice(user_choice, answer, score):
    if user_choice == answer:
        score += 1
        message = f"That's correct. Your total score is: {score}"
        return message, False, score
    else:
        message = f"Sorry, that's wrong. Your final score is: {score}"
        return message, True, score

print(logo)

def play_game(game_over, score):
    while not game_over:
        answer = pick_random()
        user_choice = (input("Who has more followers?  Type 'A' or 'B': ")).upper()
        round_result = check_choice(user_choice, answer, score)
        message = round_result[0]
        score = round_result[2]
        print(message)
        game_over = round_result[1]
        
play_game(game_over, score)

