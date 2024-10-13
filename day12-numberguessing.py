import random

logo = """
  ________                             ___________.__              _______               ___.                 
 /  _____/ __ __  ____   ______ ______ \__    ___/|  |__   ____    \      \  __ __  _____\_ |__   ___________ 
/   \  ___|  |  \/ __ \ /  ___//  ___/   |    |   |  |  \_/ __ \   /   |   \|  |  \/     \| __ \_/ __ \_  __ \
\    \_\  \  |  |  ___/ \___ \ \___ \    |    |   |   Y  \  ___/  /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \______  /____/ \___  >____  >____  >   |____|   |___|  /\___  > \____|__  /____/|__|_|  /___  /\___  >__|   
        \/           \/     \/     \/                  \/     \/          \/            \/    \/     \/       
"""


def play_game(difficulty):
    if difficulty == "easy":
        lives = 10
    else:
        lives = 5

    while lives != 0:
        print(f"You have {lives} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess > guess_number:
            print("Too high.\nGuess again.")
            lives -= 1
        elif guess < guess_number:
            print("Too low.\nGuess again.")
            lives -= 1
        elif guess == guess_number:
            print(f"You got it! The answer was {guess_number}.")
            lives = 0

    print("You've run out of guesses. You lose.")


guess_number = random.randint(1, 100)
play_again = True

while play_again:
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 to 100.")
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    play_game(level)
    if input("Do you wish to play again? Type 'y' or 'n': ") == "y":
        play_again = True
        print("\n" * 20)
    else:
        play_again = False
