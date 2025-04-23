import random

ROCK = 'r'
SCISSORS = 's'
PAPER = 'p'

emojis = {ROCK: '✊', PAPER: '✋', SCISSORS: '✌️'}
choices = tuple(emojis.keys())

def user_choices():
    while True:
        user = input("Rock, Paper or Scissors (r/p/s): ").lower()
        if user in choices:
            return user
        else:
            print('Invalid choice!')

def display_choices(user, comp_choice):
    print(f"\nYou chose: {emojis[user]}")
    print(f"Computer chose: {emojis[comp_choice]}")

def determining_winner(user, comp_choice):
    if user == comp_choice:
        print("It's a Tie!")
    elif (
        (user == ROCK and comp_choice == SCISSORS) or 
        (user == SCISSORS and comp_choice == PAPER) or 
        (user == PAPER and comp_choice == ROCK)
    ):
        print("You win! 🎉")
    else:
        print("Computer wins! 💻")

def play_game():
    while True:
        user = user_choices()
        comp_choice = random.choice(choices)

        display_choices(user, comp_choice)
        determining_winner(user, comp_choice)

        want_continue = input("\nPlay again? (y/n): ").lower()
        if want_continue != 'y':
            print("Thanks for playing!")
            break

play_game()
