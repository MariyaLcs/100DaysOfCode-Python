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

if player==0:
  print(rock)
elif player==1:
  print(paper)
elif player==2:
  print(scissors)

rundom_num = random.randint(0,2)
computer = [rock, paper, scissors][rundom_num]
print(f"Computer chose:\n {computer} {rundom_num}")


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
else:
    print("You typed an invalid number. You lose")