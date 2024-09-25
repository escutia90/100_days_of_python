print("Welcome to the blind auction program!\n")

bidStatus = {}
moreBidders = "yes"

while moreBidders == "yes": 

    name = input("What is your name?: ")
    bid = int(input("What is your bid?: ")) 
    moreBidders = input("Are there any more bidders?: ").lower()
    bidStatus[name]=bid

maxBid = 0
person = ""
for i in bidStatus:
    if bidStatus[i] > maxBid:
        maxBid = bidStatus[i]
        person = i

print(f"the winner is {person}")