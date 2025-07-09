import art

print(art.logo)
        
def winner():
    winner_person = ""
    highest_bid = 0
    for bider in database :
        bid_amount = database[bider]
        if bid_amount > highest_bid :
            highest_bid = bid_amount
            winner_person = bider
    print(f"the winner is {winner_person} with the bid of ${highest_bid}")
    
    
database = {}


continue_biding = True
while continue_biding :
    name = input("enter your name : ")
    bid = int(input("what is your bid  : $" ))
    database[name] = bid
    question = input("anyone want to bid if yes type 'yes' if no than type 'no'\n ")
    if question == "no":
        continue_biding = False
    else:
        continue
    winner(database)
    
    
print(database)

