import os

suits ={'D': '♦', 'H': '♥', 'S': '♠', 'C': '♣'}
def print_hand(hand, hide_second=False):
    cards = []
    for i in range(0,len(hand)):
        if hide_second and i == 1:
            card = [
                [" ------------- "],
                ["| ?           |"],
                ["|             |"],
                ["|             |"],
                ["|             |"],
                ["|     ???     |"],
                ["|             |"],
                ["|             |"],
                ["|             |"],
                ["|           ? |"],
                [" ------------- "]
            ]
            cards.append(card)
            continue
        card_val = hand[i][:-1]
        card_suit = suits[hand[i][-1]]
        if card_val == "10":
            card = [
            [" ------------- "],
            [f"| {card_val}          |"],
            ["|             |"],
            ["|             |"],
            ["|             |"],
            [f"|      {card_suit}      |"],
            ["|             |"],
            ["|             |"],
            ["|             |"],
            [f"|          {card_val} |"],
            [" ------------- "]
            ]
            cards.append(card)
        else:
            card = [
            [" ------------- "],
            [f"| {card_val}           |"],
            ["|             |"],
            ["|             |"],
            ["|             |"],
            [f"|      {card_suit}      |"],
            ["|             |"],
            ["|             |"],
            ["|             |"],
            [f"|           {card_val} |"],
            [" ------------- "]
            ]
            cards.append(card)
    for j in range(0,11):
        print()
        for k in range(0, len(cards)):
            print(cards[k][j][0] + " ", end="")
    return

def dealer_before_turn():
    return


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    return


def player_option():
    print("Choose an option", end="")
    print(" 1: Hit   2: Stand")
    choice = input("Choice: ")
    return choice
