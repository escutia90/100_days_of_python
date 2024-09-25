import random
import os
BLACKJACK = 21
continue_playing = True
cards = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
cards_value = {
    "A" : 11,
    "2" : 2,
    "3" : 3,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "7" : 7,
    "8" : 8,
    "9" : 9,
    "10" : 10,
    "J" : 10,
    "Q" : 10,
    "K" : 10,
}
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
'-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_
      |  \/ K|                            _/ |                
      '------'                           |__/
"""
current_cards_player = []
current_cards_dealer = []
score_player = 0
score_dealer = 0
isFirstHand = True
def sum_cards(current_hand):
    total = 0
    for i in current_hand:
        total += cards_value[i]
    return total

def print_cards(curr_cards):

    ret = "["
    for i in curr_cards[:-1]:
        ret += i + ","
    ret += curr_cards[-1]
    ret += "]"
    return ret

def deal_hand(isFirstHand):
    if isFirstHand:
        current_cards_player.append(random.choice(cards))
        current_cards_player.append(random.choice(cards))
        current_cards_dealer.append(random.choice(cards))
        current_cards_dealer.append(random.choice(cards))
    else:
        current_cards_player.append(random.choice(cards))
        current_cards_dealer.append(random.choice(cards))


def calculate_current_score():
    global score_player
    global score_dealer
    score_player = sum_cards(current_cards_player)
    score_dealer = sum_cards(current_cards_dealer)

def evaluate_winner():
    global score_player
    global score_dealer
    if score_player > 21:
        return "You Lose"
    elif score_player < 21 and score_dealer > 21:
        return "You Win!"
    elif score_player < 21 and score_dealer <21:
        if score_player > score_dealer:
            return "you win!"
        elif score_dealer > score_player:
            return "You Lose"
        else:
            return "Draw"

print(logo)
deal_hand(isFirstHand)
calculate_current_score()
print(f"Your cards: {print_cards(current_cards_player)} , current score : {score_player} \n")
print(f"Computer's first card: [{current_cards_dealer[0]}] \n")
get_another = input("Type 'y' to get another card, type 'n' to pass:")
if get_another == "n":
    print(f"Your final hand: {print_cards(current_cards_player)} , final score : {score_player} \n")
    print(f"Dealer's final hand: {print_cards(current_cards_dealer)} , final score : {score_dealer} \n")
    evaluate_winner()
    isFirstHand = True
elif get_another == "y":
    isFirstHand = False
    deal_hand(isFirstHand)


    
 