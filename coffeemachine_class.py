#This is a file of implementing coffee machine project using classes(OOP concept)

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker=CoffeeMaker()
money_machine=MoneyMachine()
menu=Menu()

more_customers=True
while more_customers:
    options=menu.get_items()
    choice=input(f"What do you want?{options}")
    if choice=="off":
        more_customers=False
    elif choice=="report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink=menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
