class CoffeeMaker:
    """Models the machine that makes the coffee"""

    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }
        self.emoji={
            "water":"💧",
            "coffee":"🌰",
            "milk":"🥛"
        }

    def report(self):
        """Prints a report of all resources."""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        """Returns True when order can be made, False if ingredients are insufficient."""
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make

    def make_coffee(self, order):
        """Deducts the required ingredients from the resources."""
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name} ☕️. Enjoy!")

    def get_resources(self):
        return '/'.join(self.resources.keys())

    def refill(self, resource):
        resource = resource.lower()
        if(resource == "water"):
            self.resources["water"] += 1000
        elif(resource == "milk"):
            self.resources["milk"] += 1000
        elif(resource == "coffee"):
            self.resources["coffee"] += 1000
        else:
            print(f"Valid refill is: {self.get_resources()}")
            return
        print(f"Refill {resource} complated! {self.emoji[resource]}")
