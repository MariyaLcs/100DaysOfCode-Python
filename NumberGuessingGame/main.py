#https://repl.it/@MashaPodosinova/guess-the-number-start#main.py
from art import logo
import random

print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
print(logo)

game_number = random.randint(0, 100)
# print(f"Pssst, the correct answer is {game_number}")

level = input("Choose a difficulty. Type 'easy' or 'hard': ")

if level == "easy":
    attempt = 10
elif level == "hard":
    attempt = 5

print(f"You have {attempt} attempts remaining to guess the number.")
player_number= int(input("Make a guess: "))   

game_on = True

def attempt_counter():  
    return attempt - 1

while game_on:        
      
    if player_number > game_number:
        print("Too high,\nGuess again!\n")
        attempt = attempt_counter()
        print(f"\nYou have {attempt} attempts remaining to guess the number.")        
        player_number= int(input("Make a guess: "))  
    elif player_number < game_number:
        print("Too low,\nGuess again!\n")
        attempt = attempt_counter()
        print(f"\nYou have {attempt} attempts remaining to guess the number.")        
        player_number= int(input("Make a guess: "))  
        
    else:
        print("You got it!")
        game_on = False
    
    if attempt == 1:
        print("\nYou lost all attempts. Game Over!!!")
        game_on = False