from replit import clear
from art import logo
print(logo)
# HINT: You can call clear() to clear the output in the console.
bids = {}


def find_highest_bidder(bidding_record):
    bidding_finished = False
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    while not bidding_finished:
        name = input("What is your name?: ")
        price = int(input("What is your bid?: $"))
        bids[name] = price
        should_continue = input("Are there any other bidders? Yes / No \n")
        if should_continue == 'No':
            print(f"The winner is {winner} with a bid of ${highest_bid}")
            bidding_finished = True
            exit()
            find_highest_bidder(bids)
        elif should_continue == 'Yes':
            clear()


find_highest_bidder({"Angela": 123, "James": 321})
