"""Yes/No checking function
based on 01_yes_nov3
"""


# Functions go here..
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


# Main Routine goes here ...
show_instructions = yes_no("Have you played this game before? : ")
print(f"You entered '{show_instructions}'")
print()
having_fun = yes_no("are you having fun? : ")
print(f"You entered '{having_fun}'")
