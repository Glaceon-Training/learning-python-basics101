import random
from higher_lower_gamedata import data
from higher_lower_art import logo, vs


def format_data(account):
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}"


def get_score(user_guess, game_answer, current_score):
    """Calculate user score in the game"""
    if user_guess == game_answer:
        current_score += 1

    return current_score


def check_answer(user_guess, game_answer):
    """Check whether user guess is True or False"""
    if user_guess == game_answer:
        return True
    else:
        return False


def higher_lower_game():
    print(logo)
    score = 0
    a = random.choice(data)

    is_game_over = False

    while not is_game_over:
        b = random.choice(data)
        if a == b:
            b = random.choice(data)

        print(f"Compare A: {format_data(a)}")
        print(vs)
        print(f"Compare B: {format_data(b)}")

        if a["follower_count"] > b["follower_count"]:
            answer_alias = "a"
        else:
            answer_alias = "b"

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        score = get_score(guess, answer_alias, score)
        if check_answer(guess, answer_alias) is True:
            print(f"You're right! Current score: {score}.")
            a = b
        else:
            print("\n" * 20)
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}.")
            is_game_over = True


higher_lower_game()
