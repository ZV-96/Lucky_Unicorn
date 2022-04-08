"""Component 2 (how much) v2
Use try/accept and pull error message out of the loop"""


error = "please enter a whole number between 1 and 10\n"
valid = False

# keep asking util valid amount (1-10) has been entered
while not valid:
    try:
        # ask for input
        user_balance = int(input("How much do you want to play with $ "))

        # check if amount is to high/low
        if 0 < user_balance <= 10:
            print(f"you are playing with ${user_balance}")
            valid = True

        else:
            print(error)

    except ValueError:
        print(error)
