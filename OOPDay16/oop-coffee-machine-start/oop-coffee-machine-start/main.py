from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


turn_off = False

while not turn_off:
    options = Menu().get_items()
    order_name = input(f"\nWhat would you like? {options}: ")
    if order_name == "off":
        turn_off = True
    elif order_name == "report":
        money_machine = MoneyMachine()
        coffee_maker = CoffeeMaker()
        money_machine.report()
        coffee_maker.report()
   
    else:
        drink = Menu().find_drink(order_name)        
        #print(drink.ingredients)
        if CoffeeMaker().is_resource_sufficient(drink) and MoneyMachine().make_payment(drink.cost):                 
            CoffeeMaker().make_coffee(drink)