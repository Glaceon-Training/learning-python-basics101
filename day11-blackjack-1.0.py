import blackjack_art
import random


def user_draw_card():
    user_hand.append(random.choice(deck))


def pc_draw_card():
    pc_hand.append(random.choice(deck))


def draw_initial():
    user_draw_card()
    user_draw_card()
    pc_draw_card()
    pc_draw_card()


def show_table(user_score):
    print(f"    Your cards: {user_hand}, current score: {user_score}")
    print(f"    Computer's first card: {pc_hand[0]}")


def referee(user_score, pc_score):
    if user_score > 21:
        print("You went over. You lose.")
    elif pc_score > 21:
        print("Computer went over. You win!")
    elif user_score > pc_score:
        print("You win!")
    elif user_score == pc_score and pc_score == 21:
        print("You lose.")
    elif user_score == pc_score:
        print("It is a draw.")
    else:
        print("You lose.")


def two_aces_at_initial(user_score, pc_score):
    if user_score > 21:
        for card in user_hand:
            if card == 11:
                ace_index = user_hand.index(11)
                user_hand[ace_index] = 1
        user_score = 0
        for card in user_hand:
            user_score += card
    elif pc_score > 21:
        for card in pc_hand:
            if card == 11:
                ace_index = pc_hand.index(11)
                pc_hand[ace_index] = 1
        pc_score = 0
        for card in pc_hand:
            pc_score += card


def play_blackjack(user_score, pc_score):
    print(blackjack_art.logo)
    continue_game = True

    draw_initial()

    for card in user_hand:
        user_score += card
    for card in pc_hand:
        pc_score += card

    # debugging initial draw get 2 aces:
    two_aces_at_initial(user_score, pc_score)

    while continue_game:
        show_table(user_score)

        get_another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()

        if get_another_card == "y" and user_score <= 21:
            user_draw_card()
            user_score += user_hand[-1]
            if user_score > 21:
                for card in user_hand:
                    if card == 11:
                        ace_index = user_hand.index(11)
                        user_hand[ace_index] = 1
                user_score = 0
                for card in user_hand:
                    user_score += card
                if user_score > 21:
                    continue_game = False
                    show_table(user_score)
                    print(f"   Your final hand: {user_hand}, final score: {user_score}")
                    print(f"   Computer's final hand: {pc_hand}, final score: {pc_score}")
                    referee(user_score, pc_score)

        elif get_another_card == "n":
            while pc_score < 17:
                pc_draw_card()
                pc_score += pc_hand[-1]
                if (17 <= pc_score <= 21) or pc_score > 21:
                    continue_game = False
                    print(f"    Your cards: {user_hand}, final score: {user_score}")
                    print(f"    Computer's first card: {pc_hand}, final score: {pc_score}")
            referee(user_score, pc_score)


loop_game = True

while loop_game:
    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_hand = []
    pc_hand = []
    user_current_score = 0
    pc_current_score = 0

    start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if start_game == "y":
        play_blackjack(user_current_score, pc_current_score)
    elif start_game == "n":
        loop_game = False
    else:
        loop_game = False
        print("Invalid input.")
