#link to Repl 
#https://repl.it/@MashaPodosinova/blind-auction-start#main.py

from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)

data={}

auction_in_progress = True
while auction_in_progress:
    name = input("What is your name?: ")
    bid = int(input ("What is your bid?: £"))
    answer = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()

    data[name] = bid

    clear()
    if answer == "no":
        auction_in_progress = False

for player in data:
    highest = 0
    print(data[player])
    if data[player] > highest:
        highest = data[player]
        name = player
print(f"The winner is {name} with a bid of £{highest}")