from classes.menu import Menu, MenuItem
from classes.coffee_maker import CoffeeMaker
from classes.money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


def find_coffee_cost(menu, coffee_name):
    item=menu.find_drink(coffee_name)    
    return item.cost


while (True):
    command = input(f"What would you like? ({menu.get_items()}): ").lower()
    if (command == "report"):
        coffee_maker.report()
        money_machine.report()
    elif (command == "off"):
        print("Thank you for using our services. Come back again!")
        break
    elif (command in menu.get_items().split("/")[:-1]):
        if (coffee_maker.is_resource_sufficient(menu.find_drink(command))):
            if (money_machine.make_payment(find_coffee_cost(menu, command))):
                coffee_maker.make_coffee(menu.find_drink(command))
            else:
                print(f"The cost for {command} is {find_coffee_cost(menu, command)}")
        else:
            print("")
    elif(command in coffee_maker.get_resources().split("/")):
        coffee_maker.refill(command)