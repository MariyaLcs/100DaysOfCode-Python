from replit import clear
from art import logo
print(logo)

data=[]

auction_in_progress = True
def add_new_player(name, bid):
    new_player={}
    new_player["name"]=name
    new_player["bid"]=bid
    data.append(new_player)

highest = 0

while auction_in_progress:
    name = input("What is your name?: ")
    bid = int(input ("What is your bid?: £"))
    answer = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()   
    add_new_player(name=name, bid=bid)
    clear()
    if answer== "no":
        auction_in_progress = False
for item in range(0, len(data)):
    if data[item]["bid"] > highest:
        highest = data[item]["bid"]
        name = data[item]["name"]
print(f"The winner is {name} with a bid of £{highest}")