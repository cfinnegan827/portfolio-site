import random

cards_val = [2,3,4,5,6,7,8,9,10, 'J', 'Q', 'K', 'A']
cards_suit = ['H', 'D', 'S', 'C']
def deal_hand():
    first_card_val = cards_val[random.randint(0,12)]
    first_card_suit = cards_suit[random.randint(0,3)]
    first_card = str(first_card_val) + first_card_suit

    second_card_val = cards_val[random.randint(0,12)]
    second_card_suit = cards_suit[random.randint(0,3)]
    second_card = str(second_card_val) + second_card_suit

    return [first_card, second_card]

def deal_card():
    card_val = cards_val[random.randint(0,12)]
    card_suit = cards_suit[random.randint(0,3)]
    card = str(card_val) + card_suit
    return card

