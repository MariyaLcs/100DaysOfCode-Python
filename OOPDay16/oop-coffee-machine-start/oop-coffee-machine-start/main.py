from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


turn_off = False

while not turn_off:
    order_name = input(f"\nWhat would you like? {Menu().get_items()}: ")
    if order_name == "off":
        turn_off = True
    elif order_name == "report":
        print(CoffeeMaker().report())
    else:
        drink = Menu().find_drink(order_name)
        
        print(drink.ingredients)
        if CoffeeMaker().is_resource_sufficient(drink):
            
            user_money = MoneyMachine().make_payment(drink.cost)
            if user_money:
                CoffeeMaker().make_coffee(drink)