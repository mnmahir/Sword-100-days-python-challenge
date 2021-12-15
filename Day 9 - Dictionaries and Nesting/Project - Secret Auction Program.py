from art import logo
import os

clearConsole = lambda: os.system("cls" if os.name in ("nt", "dos") else "clear")

print(logo)

continue_bid = True
bidder = {}


def find_winner(bidder_rec):
    winner = ""
    highest = 0
    for name in bidder_rec:
        if bidder_rec[name] > highest:
            highest = bidder_rec[name]
            winner = name
    print(f"The winner is {winner} with a bid of ${highest}!")


while continue_bid:
    name = input("What is your name?: ")
    bid_price = int(input("What's your bid?: $"))

    bidder[name] = bid_price

    if input("Are there any other bidders? Type 'yes' or 'no'. ") == "no":
        continue_bid = False
    else:
        clearConsole()

find_winner(bidder)
