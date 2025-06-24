# Fortune Teller Program - Clean Version
# This program demonstrates good coding practices: KISS, DRY, SRP, SoC, Clean Code, and Documentation

import random

# Single Responsibility: Each function does one thing well
# Separation of Concerns: Logic is clearly divided between input, logic, and output

def get_user_name():
    """Gets the user's name from input."""
    name = input("Enter your name: ")
    return name.strip()

def generate_fortune():
    """Randomly selects a fortune message."""
    fortunes = [
        "You will have a great day!",
        "Success is on your horizon.",
        "Expect the unexpected.",
        "A surprise gift is coming your way."
    ]
    return random.choice(fortunes)

def display_fortune(name, fortune):
    """Displays the fortune to the user."""
    print(f"\n{name}, your fortune is: {fortune}")

# KISS: Keeping it simple and readable
# DRY: No repetition of logic or data
def main():
    """Main function to run the fortune teller."""
    user_name = get_user_name()
    fortune_message = generate_fortune()
    display_fortune(user_name, fortune_message)

# Clean Code: Clear naming, minimal nesting, logical structure
if __name__ == "__main__":
    main()
