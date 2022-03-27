from hashlib import new
import os
from art import logo
clear = os.system('clear')

print(logo)
bidder_record = {}
should_countinue = False

def find_highest_bidder(_record):
    highest = float('-inf')
    winner = ''
    for bidder in _record:
        bids = _record[bidder]
        if bids > highest:
            highest = bids
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest}")

while not should_countinue:
    bidders_name = input("What's your name?:")
    your_bid = int(input("Enter your bid:"))
    bidder_record[bidders_name] = your_bid
    new_bid = input("Are they any other bidders? Type 'yes' or 'no' : \n").lower()

    if new_bid == "no":
        should_countinue = True
        find_highest_bidder(bidder_record)
    elif new == "yes":
        clear

