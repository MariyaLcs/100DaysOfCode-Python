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

profit = 0

turn_off = False


def check_up(order_ingredients):
    """Rerurns true when order can be made"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there in not {item}")
            return False
    return True


def calc_coins():
    """Returns the total amount of money from the customer"""
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickels = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    total = quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01
    return total


def is_sufficient(money_received, price):
    """Returns true if it is enough money"""
    if price <= money_received:
        change = round(money_received - price, 2)
        print(f"Here is your {option}.Enjoy!\nHere us £{change} in change")
        global profit
        profit += price
        return True
    else:
        print(f"Sorry not enough money")
        return False


def make_cup(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️Enjoy!")


while not turn_off:
    option = input("\nWhat would you like? (espresso/latte/cappuccino): ")

    if option == "off":
        turn_off = True

    elif option == "report":
        print(f'Water : {resources["water"]}ml\n'
              f'Milk : {resources["milk"]}ml\n'
              f'Coffee : {resources["coffee"]}ml\nMoney : {profit}')
    else:

        drink = MENU[option]

        if check_up(drink["ingredients"]):
            user_money = calc_coins()
            if is_sufficient(user_money, drink["cost"]):
                make_cup(option, drink["ingredients"])