from random import randint
from game_data import data
from replit import clear
from art import logo, vs
print(logo)

score = 0
game_on = True

def check_answer(player_answer, count_a, count_b):
  """Checks followers against user's guess 
  and returns True if they got it right.
  Or False if they got it wrong.""" 
  if count_a > count_b:
    return player_answer == "A"
  else:
    return player_answer == "B"

option_a = data[randint(0, len(data)-1)]
option_b = data[randint(0, len(data)-1)]

while game_on: 
    option_a = option_b   
    count_b = data[randint(0, len(data)-1)]

    while option_a == option_b:
      option_b = data[randint(0, len(data))]

    count_a = option_a['follower_count']
    count_b = option_b['follower_count']

    print(f"\nCompare A: {option_a['name']}, a {option_a['description']}, from {option_a['country']}.")
    print(vs)
    print(f"Compare B: {option_b['name']}, a {option_b['description']}, from {option_b['country']}.")

    player_answer = input("\nWho has more followers? Type 'A' or 'B': ").upper()

    is_correct = check_answer(player_answer, count_a, count_b)
    clear()
    if is_correct:
      score += 1
      print(f"You're right! Current score: {score}.")
    else:
      game_on = False
      print(f"Sorry, that's wrong. Final score: {score}")
