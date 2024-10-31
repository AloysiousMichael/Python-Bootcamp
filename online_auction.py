logo = r"""
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
"""

print(logo)


bids = {}

def max_bid(bidding_list):
    highest_amount=0
    winner=" "
    for bidder in bidding_list:
        bid_amount=bidding_list[bidder]
        if bid_amount > highest_amount:
            highest_amount=bid_amount
            winner=bidder
    print(f"The winner is {winner} with an bid amount of {highest_amount} .")


continue_biding=True
while continue_biding:
    name = input("What is your name ?: ")
    price = int(input("Enter your bid amount $ : "))
    bids[name] = price
    should_continue = input("Is any bidders left . Type 'yes' or 'no'. ").lower()
    if should_continue=="no":
        max_bid(bids)
        continue_biding=False
    else:
        print(" \n "*200)
        continue_biding=True




