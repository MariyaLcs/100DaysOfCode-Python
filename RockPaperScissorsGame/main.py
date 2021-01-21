import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Rock, Paper, Scissors Game")
player = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors \n"))

if player>2 or player<0:
  print("You typed an invalid number. You lose")

else:
  game_images=[rock, paper, scissors]
  print(game_images[player])


  rundom_num = random.randint(0,2)
  computer = game_images[rundom_num]
  print(f"Computer chose: {rundom_num}\n {computer}")


  if player==rundom_num:
    print("Drow")
  elif player==0:  
    if rundom_num==2:
      print("You win")
    else:
      print("You lose")
  elif player==1:
    if rundom_num==0:
      print("You win")
    else:
      print("You lose")
  elif player==2:
    if rundom_num==1:
      print("You win")
    else:
      print("You lose")
