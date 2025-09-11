import deal
import utils
import bets

def player_hand(hand, dealer_hand):
    if check_blackjack(hand):
        print("Blackjack!!!")
        return val, hand
    else:
        while(True):
            if check_blackjack(hand):
                utils.clear_screen()
                utils.print_hand(dealer_hand,hide_second=True)
                print("\n")
                utils.print_hand(hand)
                print("Player: ", hand_val(hand))
                print("Blackjack!!")
                break
            val = hand_val(hand)
            utils.clear_screen()
            utils.print_hand(dealer_hand, hide_second=True)
            print("\n")
            utils.print_hand(hand)
            print("Player: ", hand_val(hand))
            if val > 21:
                utils.clear_screen()
                utils.print_hand(dealer_hand, hide_second=True)
                print("\n")
                utils.print_hand(hand)
                print("Player: ", hand_val(hand))
                print("Bust!!")
                break
            choice = utils.player_option()
            if choice == "1":
                hand = hit(hand)
            elif choice == "2":
                break
        val = hand_val(hand)
        return val, hand

def dealer_hand(hand, player_hand):
    # dealer must stand on a 16
    print(hand)
    if check_blackjack(hand):
        utils.print_hand(hand)
        print("Dealer: ", hand_val(player_hand))
        print("\n")
        utils.print_hand(player_hand)
        print("Player: ", hand_val(player_hand))
        return
    else:
        dealer_hand_val = hand_val(hand)
        utils.clear_screen()
        utils.print_hand(hand)
        print("Dealer: ", hand_val(hand))
        print("\n")
        utils.print_hand(player_hand)
        print("Player: ", hand_val(player_hand))
        while(dealer_hand_val < 16):
            utils.clear_screen()
            utils.print_hand(hand)
            print("Dealer: ", hand_val(hand))
            print("\n")
            utils.print_hand(player_hand)
            print("Player: ", hand_val(player_hand))
            hand = hit(hand)
            dealer_hand_val = hand_val(hand)

        if dealer_hand_val >= 16 and dealer_hand_val < 21:
            #stands
            utils.clear_screen()
            utils.print_hand(hand)
            print("Dealer: ", hand_val(hand))
            print("\n")
            utils.print_hand(player_hand)
            print("Player: ", hand_val(player_hand))
            return dealer_hand_val
        elif dealer_hand_val > 21:
            utils.clear_screen()
            utils.print_hand(hand)
            print("Dealer: ", hand_val(hand))
            print("\n")
            utils.print_hand(player_hand)
            print("Player: ", hand_val(player_hand))
            return dealer_hand_val
        elif dealer_hand_val < 16:
            hand = hit(hand)
            return dealer_hand_val

def hit(hand):
    new_card = deal.deal_card()
    new_hand = []
    for card in hand:
        new_hand.append(card)
    new_hand.append(new_card)
    return new_hand

def check_blackjack(hand):
    val = hand_val(hand)
    if val == 21:
        return True
    else:
        return False

def hand_val(hand):
    value = 0
    aces = 0
    for card in hand:
        val = check_face(card[:-1], 0)
        if card[:-1] == 'A':
            aces += 1
        value += val

    # Adjust for aces (count them as 1 instead of 11 if needed)
    while value > 21 and aces > 0:
        value -= 10
        aces -= 1

    return value


def card_val(card):
    val = check_face(card)
    return val

face_cards = ['J', 'Q', 'K']
def check_face(card_val, ace_over):
    if card_val in face_cards:
        return 10
    elif card_val == 'A' and ace_over == 0:
        return 11
    elif card_val == 'A' and ace_over == 1:
        return 1
    else:
        return int(card_val)


def check_outcome(player_val, dealer_val, bet):
    if player_val > 21 and dealer_val < 21:
        print("Player Bust, Dealer wins!")
        bets.payout(0, bet)
        return
    elif player_val < 21 and dealer_val > 21:
        print("Dealer Bust, Player wins!")
        bets.payout(1, bet)
        return
    elif player_val > dealer_val:
        print("Player wins!")
        bets.payout(1, bet)
    elif player_val < dealer_val:
        print("Dealer wins!")
        bets.payout(0, bet)
    elif player_val > 21 and dealer_val > 21:
        print("Push!")
    elif player_val == dealer_val:
        print("Push!")
    return