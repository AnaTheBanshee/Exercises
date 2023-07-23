import random  # Imports random module

"""
Rock,paper,scissors uses "Rock>Scissors>Paper>Rock" forming a triangle of values of which of them wins
We use comparison with nested functions because of simpler syntax;meaning less lines
We use While so we could repeat the game with break option for stopping.
"""

while True:
    user_pick = input("Pick Rock,Paper or Scissors:\n")  # used as print and input at once
    x = random.randint(1, 3)  # To include 3 random numbers\values for rng use
    if x == 1:
        generator = 'Rock'
    elif x == 2:
        generator = 'Paper'
    else:
        generator = 'Scissors'
    print(f"\nUser pick {user_pick},\nGenerator picked {generator}.\n")  # prints values that got picked
    if user_pick == generator:  # if both sides picked same
        print(f"It's a tie.")  # used format because of {} values
    elif user_pick == "Rock":
        if generator == "Scissors":
            print(f"User wins.")
        else:
            print(f"User loses.")
    elif user_pick == "Paper":
        if generator == "Rock":
            print(f"User wins.")
        else:
            print(f"User loses.")
    elif user_pick == "Scissors":
        if generator == "Paper":
            print(f"User wins.")
        else:
            print(f"User loses.")
    else:
        print("It is not included.")
    # In case if we want to stop the game
    play_again = input(f"\nPlay again? (yes/no): ")
    if play_again.lower() != "yes":
        break
