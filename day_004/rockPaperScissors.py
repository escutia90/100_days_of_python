import random as rnd
choice=['Rock', 'Paper', 'Scissors']
while True:
    i = input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n")
    i = int(i)
    c = rnd.randint(0,2)
    print(f"Computer chose {choice[c]}")
    if i == c:
        print("Tie! try again\n")
    elif i == 0 and c == 1:
        print("You lose\n")
    elif i == 0 and c == 2:
        print("You WIN!\n") 
    elif i == 1 and c == 0:
        print("You lose\n")        
    elif i == 1 and c == 2:
        print("You WIN!\n") 
    elif i == 2 and c == 0:
        print("You lose\n")  
    elif i == 2 and c == 1:
        print("You lose\n")  
