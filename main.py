from art import *
print(logo)
auction = {}
bidding_finished = False

def find_highest_bidder(bidding_record):

    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with the highest bid amount of Rs{highest_bid}.")

while not bidding_finished:
    names = input("Name of the bidder: ")
    bids = int(input("How much amount would you bid for: "))
    auction[names] = bids
    users = input("Are there any other bidders left? "). lower()
    if users == "no":
        bidding_finished = True
        find_highest_bidder(auction)