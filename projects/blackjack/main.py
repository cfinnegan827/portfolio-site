import hand
import deal
import utils
import bets

def main():
    utils.clear_screen()
    bet = bets.place_bet()
    dealer_hand = deal.deal_hand()
    player_hand = deal.deal_hand()
    if hand.check_blackjack(dealer_hand):
        print("Dealer has Blackjack!!")
        bets.payout(0,bet)
        replay = int(input("Play Again (1=YES 2=NO): "))
        if replay == 1:
            main()
        else:
            return
    elif hand.check_blackjack(player_hand):
        print("Player has Blackjack!!")
        bets.payout(1,bet)
        replay = int(input("Play Again (1=YES 2=NO): "))
        if replay == 1:
            main()
        else:
            return
    else:
        player_val,new_hand = hand.player_hand(player_hand, dealer_hand)
        dealer_val = hand.dealer_hand(dealer_hand, new_hand)
        hand.check_outcome(player_val, dealer_val, bet)
        replay = int(input("Play Again (1=YES 2=NO): "))
        if replay == 1:
            main()
        else:
            return

main()