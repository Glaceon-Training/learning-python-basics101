import auction_art

print(auction_art.logo)

continue_auction = True
auction = {}


def highest_bidder(auction_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in auction_dictionary:
        bid_amount = auction_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}.")


while continue_auction:
    name = str(input("What is your name?: "))
    bid = int(input("What is your bid?: $"))
    auction[name] = bid
    ask = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if ask == "yes":
        print("\n" * 20)
    elif ask == "no":
        highest_bidder(auction_dictionary=auction)
        print(auction)
        continue_auction = False
