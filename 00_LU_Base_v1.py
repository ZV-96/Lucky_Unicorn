"""LU base component
components added after they have been created and tested"""


# Functions

# Yes/No Checker Function
def yes_no(question_text):
    while True:

        # Ask the user if they have played before
        answer = input(question_text).lower()

        # if they say yes, output 'Program Continues'
        if answer == "yes" or answer == "y":
            answer = "Yes"
            return answer

        # If they say no, output 'display Instructions'
        elif answer == "no" or answer == "n":
            answer = "No"
            return answer

        # Otherwise - show error
        else:
            print("Please answer 'yes' or 'no'")


# Function that displays instructions
def instructions():
    print("***** How to Play *****")
    print()
    print("The rules of the game will go here")
    print()


# number checking function
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


# Main Routine goes here ...
played_before = yes_no("Have you played this game before? : ")

if played_before == "No":
    instructions()

# ask how much they want to play with
user_balance = num_check("How much do you want to play with $", 1, 10)
print(f"you are playing with ${user_balance}")

