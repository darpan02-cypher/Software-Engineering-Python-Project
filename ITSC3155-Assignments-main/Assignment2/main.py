import data
from sandwich_maker import SandwichMaker
from cashier import Cashier



# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()







def main():
    ###  write the rest of the codes ###
    while True:
            choice = input("What would you like? (small/medium/large/off/report): ")
            if choice == "off":
                break
            elif choice == "report":
                print(f"Bread: {sandwich_maker_instance.machine_resources['bread']} slices")
                print(f"Ham: {sandwich_maker_instance.machine_resources['ham']} slices")
                print(f"Cheese: {sandwich_maker_instance.machine_resources['cheese']} ounces")
            elif choice in recipes:
                ingredients = recipes[choice]["ingredients"]
                if sandwich_maker_instance.check_resources(ingredients):
                    payment = cashier_instance.process_coins()
                    if cashier_instance.transaction_result(payment, recipes[choice]["cost"]):
                        sandwich_maker_instance.make_sandwich(choice, ingredients)
                        print(f"Here is your {choice} sandwich. Enjoy!")
            else:
                print("Invalid input. Please select a valid option.")

if __name__=="__main__":
    main()
