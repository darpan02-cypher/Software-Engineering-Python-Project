# This is the horrible version. It's intentionally bad!
# Violates: DRY, SRP, KISS, Clean Code, Comments, YAGNI, SoC

import random

# Everything is dumped in one place. No clear responsibilities. Bad naming and formatting.

def doEverything():
    # This does too much. Violates Single Responsibility.
    # No separation of concerns. Input, logic, and output all mixed up.
    # Not KISS. Confusing logic and hard to follow.
    x = input("What's your name?      ")  # Not stripped
    fortunes1 = "You will have a great day!"
    fortunes2 = "Success is on your horizon."
    fortunes3 = "Expect the unexpected."
    fortunes4 = "A surprise gift is coming your way."
    # Repeating similar logic four times instead of using a list. Violates DRY.
    pick = random.randint(1,4)
    if pick == 1:
        print("Hey " + x + ", " + fortunes1)
    elif pick == 2:
        print("Hey " + x + ", " + fortunes2)
    elif pick == 3:
        print("Hey " + x + ", " + fortunes3)
    elif pick == 4:
        print("Hey " + x + ", " + fortunes4)

    # Useless code added for no reason. Violates YAGNI (You Aren't Gonna Need It)
    print("Processing complete.")  
    for i in range(3):
        print("...")  # Adds no value

# No comments on what the function does. Poor documentation.
# Bad naming: "doEverything" says nothing.

doEverything()
