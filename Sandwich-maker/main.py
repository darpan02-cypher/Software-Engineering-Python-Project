### Data ###
#recipes are stored in a dictionary, whereas small, medium and large are the keys
recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

# resources is stored in a dictionary
resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    #constructor- it is used to initialize the class,  It runs when you create a new SandwichMachine object. It saves the recipes, resources, and the machine's resources (which you give as input) so the object can use them later.
    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.recipes = recipes
        self.resources = resources
        self.machine_resources = machine_resources # this line is used to bind the input variable to self variable ,

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        """ Hint: use the resources dictionary to check if the ingredients are sufficient."""
        for item in ingredients: #here, item is the key of ingredients, to check if the ingredients are sufficient i.e. "bread", "ham", "cheese"
            if ingredients[item] > self.machine_resources[item]:
                print(f"Sorry, there is not enough {item}.")
                return False
        return True

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        print("Please insert coins.")
        dollars = int(input("How many large dollars?: ")) * 1.00
        half_dollars = int(input("How many half dollars?: ")) * 0.50
        quarters = int(input("How many quarters?: ")) * 0.25
        nickels = int(input("How many nickels?: ")) * 0.05
        total = dollars + half_dollars + quarters + nickels
        return total

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        
        if coins >= cost:
            change = round(coins - cost, 2) # rounding the change to 2 decimal places
            if change > 0:
                print(f"Here is ${change} in change.")
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            return False

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        for item, amount in order_ingredients.items():
            self.machine_resources[item] -= amount


### Make an instance of SandwichMachine class and write the rest of the codes ###
sandwich_maker = SandwichMachine(resources)


def main():
    while True:
        choice = input("What would you like? (small/medium/large/off/report): ")
        if choice == "off":
            break
        elif choice == "report":
            print(f"Bread: {sandwich_maker.machine_resources['bread']} slices")
            print(f"Ham: {sandwich_maker.machine_resources['ham']} slices")
            print(f"Cheese: {sandwich_maker.machine_resources['cheese']} ounces")
        elif choice in sandwich_maker.recipes:
            ingredients = sandwich_maker.recipes[choice]["ingredients"]
            if sandwich_maker.check_resources(ingredients):
                payment = sandwich_maker.process_coins()
                if sandwich_maker.transaction_result(payment, sandwich_maker.recipes[choice]["cost"]):
                    sandwich_maker.make_sandwich(choice, ingredients)
                    print(f"Here is your {choice} sandwich. Enjoy!")
        else:
            print("Invalid input. Please select a valid option.")


if __name__ == "__main__":
    main()
