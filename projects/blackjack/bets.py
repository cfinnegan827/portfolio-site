def place_bet():
    balance = get_balance()
    print("Current Balance: ", balance)
    bet = int(input("Place a bet: "))
    if bet == 0 or bet > balance:
        print("Invalid Bet")
        place_bet()
    else:
        return bet

def payout(outcome, bet):
    #win = 1
    #loss = 0
    balance = int(get_balance())
    if outcome == 1:
        payout = balance + int(bet + (bet * 0.5))
        with open("balance.txt", "w") as file:
            file.write(str(payout))
    elif outcome == 0:
        payout = balance - bet
        with open("balance.txt", "w") as file:
            file.write(str(payout))
    
    return

def get_balance():
    with open("balance.txt", "r") as file:
        temp = file.read()
    balance = int(temp)
    return balance
