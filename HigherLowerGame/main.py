#http://www.higherlowergame.com/
# https://repl.it/@MashaPodosinova/higher-lower-start#main.py

from random import randint
from game_data import data
# from replit import clear
from art import *
print(logo)

score = 0
game_on = True

while game_on: 

    option_a = data[randint(0, len(data)-1)]
    option_b =data[randint(0, len(data)-2)]
    count_a = option_a['follower_count']
    count_b = option_b['follower_count']

    if count_a  > count_b:
        letter = "A"
        right_answer = option_a 
    else:
        letter = "B"
        right_answer = option_b
   
    print(f"\nCompare A: {option_a['name']}, a {option_a['description']}, from {option_a['country']}.")
    print(vs)
    print(f"Compare A: {option_b['name']}, a {option_b['description']}, from {option_b['country']}.")

    player_answer = input("\nWho has more followers? Type 'A' or 'B': ").upper()

    if player_answer == letter:
        score += 1
        print(f"\nYou're right!  Current score: {score}.")
        option_a = right_answer
        option_b = data[randint(0, len(data)-1)]
        
    else:
        print(f"\nYou're wrong!  Current score: {score}. Game Over!")
        game_on = False
