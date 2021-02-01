#https://repl.it/@MashaPodosinova/coffee-machine-start#main.py
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0

turn_off = False


def make_cup(user_money, price):

    if price <= user_money:
        change = round(user_money - price, 2)
        print(f"Here is your {option}.Enjoy!\nHere us £{change} in change")
        global money
        money += price
        print(money)
        return money
    else:
        print(f"Sorry not enough money")


while not turn_off:
    option = input("\nWhat would you like? (espresso/latte/cappuccino): ")

    if option == "report":
        print(f'Water : {resources["water"]}ml\n'
              f'Milk : {resources["milk"]}ml\n'
              f'Coffee : {resources["coffee"]}ml\nMoney : {money}')
        option = input("\nWhat would you like? (espresso/latte/cappuccino): ")

    price = MENU[option]["cost"]

    if option == "espresso":
        milk = 0
    else:
        milk = MENU[option]["ingredients"]["milk"]

    water = MENU[option]["ingredients"]["water"]
    coffee = MENU[option]["ingredients"]["coffee"]

    if resources["water"] >= water and resources["milk"] >= milk and resources["coffee"] >= coffee:
        resources["water"] -= water
        resources["milk"] -= milk
        resources["coffee"] -= coffee
        # print(resources)
        quarters = int(input("how many quarters?: "))
        dimes = int(input("how many dimes?: "))
        nickels = int(input("how many nickles?: "))
        pennies = int(input("how many pennies?: "))
        user_money = round(quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01, 2)

        make_cup(user_money, price)
    else:
        if resources["water"] < water:
            print("Sorry there in not enough water")
        if resources["milk"] < milk:
            print("Sorry there in not enough milk")
        if resources["coffee"] < water:
            print("Sorry there in not enough coffee")
        turn_off = True






