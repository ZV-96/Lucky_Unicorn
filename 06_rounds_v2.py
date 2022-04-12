"""Component 4 - Game mechanics and looping v2
based on 06_rounds_v1
Removed hard-wiring so that all tokens can be allocated (radiant 1-100)
gives user feedback about number of rounds and maintains balance.
test amount set to $5
"""


import random

# Main routine
TEST_AMOUNT = 5
balance = TEST_AMOUNT

rounds_played = 0
play_again = ""

# testing loop to generate 5 tokens
while play_again != "x":
    rounds_played += 1  # keep track of rounds
    number = random.randint(1, 100)  # can only be donkey

    # adjust balance
    # if the random number is between 1 and 5
    # user gets a unicorn and $4 to balance
    if 1 <= number <= 5:
        token = "unicorn"
        balance += 4

    # if the random number is between 6 and 36
    # user gets a donkey (subtract $1 from balance)
    elif 6 <= number <= 36:
        token = "donkey"
        balance -= 1

    # in all other cases the token must be a horse or a zebra
    # (subtract $0.50 from the balance in either case)
    else:
        # if number is even set the token to zebra
        if number % 2 == 0:
            token = "zebra"
            balance -= 0.5
        # otherwise, set the token to horse
        else:
            token = "horse"
            balance -= 0.5

    # output
    print(f"Round {rounds_played}. Token: {token}, Balance: ${balance:.2f}")
    if balance < 1:
        print("\nSorry you have run out of money")
        play_again = "x"
    else:
        play_again = input("\nDo you want to play another round?\n<enter> to play"
                           "again or 'X' to exit").lower()
    print()

print("Thanks for playing!")
print(f"You started with: ${TEST_AMOUNT:.2f}")
print(f"and leave with :{balance:.2f}")
print("Goodbye")



