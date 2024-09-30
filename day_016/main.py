from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

main_menu = Menu()
coffe_maker = CoffeeMaker()
money_machine = MoneyMachine()

available_items = main_menu.get_items()
is_on = True
while is_on:
    choice = input(f"what would you like? {available_items}?:")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffe_maker.report()
        money_machine.reports()
    else:
        selected_drink = main_menu.find_drink(choice)
        if selected_drink != None:
            hasEnoughResources = coffe_maker.is_resource_sufficient(selected_drink)
            if hasEnoughResources == True:
                isPayOk = money_machine.make_payment(selected_drink.cost)
                if isPayOk == True:
                    coffe_maker.make_coffee(selected_drink)

        
