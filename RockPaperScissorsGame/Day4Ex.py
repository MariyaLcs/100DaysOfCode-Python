#Ex1 Heads or Tails
import random

coin = random.randint(0,1)
if coin==1:
  print("Heads")
else:
  print("Tails")

print(coin)

#Ex2 Who's Paying

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

####################################

#Angela, Ben, Jenny, Michael, Chloe
import random

winner_number = random.randint(0, len(names))
winner = names[winner_number]

#OR
#winner = random.choice(names)

print(winner)

#Ex3 Treasure Map

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

####################################

x_coordinate = int(position[0])
y_coordinate = int(position[1])
# print(x_coordinate, y_coordinate)
map[y_coordinate-1][x_coordinate-1]="X"