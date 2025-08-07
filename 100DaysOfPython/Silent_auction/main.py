from art import logo
print(logo)

bid_dic = {}
def find_winner(bid_dic):
    max_bid = 0
    bidder = ""
    for name in bid_dic:
        if bid_dic[name] >= max_bid:
            max_bid = bid_dic[name]
            bidder = name
    print(f"The winner is {bidder} with {max_bid}$!!!")

while True:
    name = input("What is your name? ")
    bid = int(input("How much do you bid? "))
    bid_dic[name] = bid

    more_bids = input("Are there any other bidders? type 'yes' or 'no':\n").lower()
    if more_bids == "yes":
        print("\n" * 20)
        continue
    elif more_bids == "no":
        print("\n" * 20)
        find_winner(bid_dic)
        break

