MAX_BALANCE = 1000


class CoinMachine:
    def __init__(self):
        self.bets = {
            'Line-1': None,
            'Line-2': None,
            'Line-3': None,
            'Diagonal-1': None,
            'Diagonal-2': None
        }
        self.bet_amount = None
        self.balance = None

        while True:
            try:
                print(f"You may start with up to --{MAX_BALANCE} coins-- for a session")
                user_balance = int(input("Enter your starting balance: "))
                if user_balance < 0 or user_balance > MAX_BALANCE:
                    # print("Balance Out-of-Bounds")
                    raise ValueError
                else:
                    self.balance = user_balance
                    break
            except ValueError:
                print(">> You may have entered an Invalid Character\n>> Please enter a valid number\n")
                continue

    def get_balance(self):
        return self.balance

    def get_bets(self):
        # Initialise all line_bets to 'no'
        for line in self.bets.keys():
            self.bets[line] = 'n'
        count = None

        while True:
            try:
                count = 0
                for line in self.bets.keys():
                    # Get which lines to bet on
                    bet_on_line = input(f"Would you like to bet on {line} [y/n]: ")[0].lower()
                    assert bet_on_line in ['y', 'n']
                    if bet_on_line == 'y':
                        # update bets dictionary
                        self.bets[line] = 'y'
                        count += 1
                break
            except AssertionError:
                print(">> You may have entered an Invalid Character\n>> Only 'y' or 'n' are required inputs\n")
                continue

        while True:
            try:
                # Get bet_amount for 1 line from user
                self.bet_amount = int(input("How much would you like to bet on each line: "))
                # Multipy bet_amount with total lines user has bet on and check for available balance
                total_bet_amount = self.bet_amount * count
                if 0 > total_bet_amount or total_bet_amount > self.balance:
                    raise ValueError
                break
            except ValueError:
                print(">> You may have entered an Invalid Character or your total bets exceed your balance\n"
                      ">> Please enter a valid number\n")

    def calculate_payout(self, rack_obj):
        pass
