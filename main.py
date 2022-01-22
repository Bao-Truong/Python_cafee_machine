import os
import coin_values
from recipe import MENU


def clear(): return os.system("cls") if os.name == "nt" else os.system("clear")


SPACE = 50

resources = {
    "water": 3000,
    "milk": 200,
    "coffee": 100,
    "moneys": 0
}


def coin_change(total_value, price):
    return round(total_value-price, 2)


def coin_check(inserted, coffee_name):
    total_value = inserted[0]*coin_values.QUARTERS + inserted[1]*coin_values.DIMES + \
        inserted[2]*coin_values.NICKLES+inserted[3]*coin_values.PENNIES
    if(total_value > MENU[coffee_name]["cost"]):
        return coin_change(total_value, MENU[coffee_name]["cost"])
    elif(total_value < MENU[coffee_name]["cost"]):
        return -1
    else:
        return 0


def coin_management(coffee_name: str):
    print("Please insert coins")
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickles = float(input("How many nickles?: "))
    pennies = float(input("How many pennies?: "))
    inserted = [quarters, dimes, nickles, pennies]
    coin_status = coin_check(inserted, coffee_name)
    if(coin_status < 0):
        print(f"Insufficient coin, the price is {load_cost(coffee_name)}")
        return False
    elif(coin_status > 0):
        print(f"Here is ${coin_status} in change")
    return True


def check_resources_available(coffee_name: str):

    required_ingredients = load_recipe(coffee_name)
    reqr_water = required_ingredients["water"]
    reqr_coffee = required_ingredients["coffee"]
    reqr_milk = 0 if required_ingredients.get(
        "milk", None) == None else required_ingredients["milk"]
    curt_water = resources["water"]
    curt_coffee = resources["coffee"]
    curt_milk = resources["milk"]

    if(reqr_water > curt_water):
        print("Sorry there is not enough water")
        return False
    if(reqr_coffee > curt_coffee):
        print("Sorry there is not enough coffee")
        return False
    if(reqr_milk > curt_milk and reqr_milk > 0):
        print("Sorry there is not enough milk")
        return False
    return True


def load_recipe(coffee_name):
    return MENU[coffee_name]["ingredients"]


def load_cost(coffee_name):
    return float(MENU[coffee_name]['cost'])


def deliver_coffee(coffee_name):
    print(f"Here is your {coffee_name}, Enjoy! ☕")


def pour_coffee(coffee_name):
    global resources
    resources["moneys"] += load_cost(coffee_name)
    ingredients = load_recipe(coffee_name)
    resources["water"] -= int(ingredients["water"])
    resources["coffee"] -= int(ingredients["coffee"])
    if("milk" in ingredients):
        resources["milk"] -= int(ingredients["milk"])
    deliver_coffee(coffee_name)


def make_coffee(coffee_name):
    """Check resources then make coffe or reject making

    Args:
        coffee_name (str): [description]
    """
    print(f"You are ordering {coffee_name}, we will bring it on right away!")
    resource_avail = check_resources_available(coffee_name)
    if(resource_avail):
        coin_completed = coin_management(coffee_name)
        if(coin_completed):
            pour_coffee(coffee_name)


def report():
    metrics = {
        "water": "ml",
        "milk": "ml",
        "coffee": "g",
        "moneys": "$"
    }
    print("-"*SPACE)
    for k, v in resources.items():
        print(f"{k.title()}: {v}{metrics[k]}")
    print("-"*SPACE)


def water():
    global resources
    resources["water"] += 1000
    print("> Refill water Success!💧")


def coffee():
    global resources
    resources["coffee"] += 1000
    print("> Refill coffee Success!🌰")


def milk():
    global resources
    resources["milk"] += 1000
    print("> Refill milk Success!🥛")


def print_menu():
    clear()
    print("Today Coffee☕\t\t Price")
    for i, coffee_name in enumerate(MENU.keys()):
        print(f"{i+1}. {coffee_name.title()} \t\t ${load_cost(coffee_name)}")


def help():
    print("*"*SPACE)
    print("Type options:")
    print(f"'menu': \t\t\t Show today coffee menu")
    print(f"'report': \t\t\t Show current resources of water/coffee/milk/moneys")
    print(f"'off':  \t\t\t Turn off the coffee machine")
    print(f"'<coffee_name>': \t\t\t Type the Coffe name to order")
    print("*"*SPACE)
    print("Refill resources options:")
    print(f"'water': \t\t\t Refill 1000 of water")
    print(f"'milk': \t\t\t Refill 1000 of milk")
    print(f"'coffee': \t\t\t Refill 1000 of coffee")
    print("*"*SPACE)


def machine_router(command):
    refill = {"water": water, "coffee": coffee, "milk": milk}
    if(command == "report"):
        report()
    elif(command == "menu"):
        print_menu()
    elif(command in list(MENU.keys())):
        make_coffee(command)
    elif(command in ["water", "coffee", "milk"]):
        refill[command]()
    elif(command == "off"):  # Shutdown
        return True
    else:
        help()
    # No Shutdown, Continue Working
    return False


def load_menu():
    return "/".join(MENU.keys())


def cafee_machine():
    print_menu()
    while(True):
        command = input(
            f"What would you like? ({load_menu()}): ").lower()
        shutdown = machine_router(command)
        if(shutdown):
            print("Thank you for using our services, comeback again!")
            break


cafee_machine()
