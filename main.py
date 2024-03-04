from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
menu = Menu()
cash_register = MoneyMachine()
machine_on = True

while machine_on:
    drink_order = input(f"What would you like? {menu.get_items()}")
    order = menu.find_drink(drink_order)
    if drink_order == "report":
        coffee_machine.report()
        cash_register.report()
    elif drink_order == "off":
        break
    else:
        if not coffee_machine.is_resource_sufficient(order):
            break
        else:
            cash_register.make_payment(order.cost)
            coffee_machine.make_coffee(order)
