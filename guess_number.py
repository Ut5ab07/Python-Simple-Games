import random

num = random.randint(1,100)
while True:
    guess= int(input("Guess the number between 1 to 100"))

    if guess>100:
        print("Invalid choice. Please choose number between 1 to 100!")

    elif guess == num:
        print(f"(Guessed right number. the correct number is {num})")
        break
    else:
        print("guessed wrong number")