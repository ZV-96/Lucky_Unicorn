"""Component 2 (how much) v4
Changing v3 into a function
Also needed to change user_balance to the more generic variable name 'response'
and to change the condition and position of the number comparison into the loop
to make the function recyclable"""


# Functions
def num_check(question, low, high):
    error = "Invalid input\n" \
        "please enter an number between {} and {}\n".format(low, high)

    # keep asking util valid amount (1-10) has been entered
    while True:
        try:
            # ask for input
            response = int(input(question))

            # check for number in required range
            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# Main Routine
user_balance = num_check("How much do you want to play with $", 1, 10)
print(f"you are playing with ${user_balance}")
