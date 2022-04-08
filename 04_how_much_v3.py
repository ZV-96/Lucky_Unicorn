"""Component 2 (how much) v3
More efficient method - includes valid range as the basis of the while loop
which eliminates the need to use the valid variable"""


# Main routine
error = "Invalid input\n"
user_balance = 0

# keep asking util valid amount (1-10) has been entered
while not 1 <= user_balance <= 10:
    try:
        # ask for input
        user_balance = int(input("Please enter a whole number between 1 and 10"
                                 "\nHow much do you want to play with $ "))
        print()

    except ValueError:
        print(error)


print(f"you are playing with ${user_balance}")
