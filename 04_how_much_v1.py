"""Component 2 (how much) v1
ask the user how much to play with and check if the input is a valid
integer between 1 and 10, if it is this amount becomes e balance
in their account"""


user_balance = int(input("how much do yo want to play with (must be an interger between 1 - 10)? $ "))

# keep asking util valid amount (1-10) has been entered
while not 1 <= user_balance <= 10:
    print("Try again, Please enter a whole number between 1 and 10")
    # ask for input
    user_balance = int(input("How much do you want to play with $ "))

print(f"you are playing with ${user_balance}")
