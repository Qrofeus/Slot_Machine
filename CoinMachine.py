from SlotRack import SYMBOL_PAYOUT, RACK_SIZE

MAX_BALANCE = 1000


class CoinMachine:
    def __init__(self, slot_rack_object):
        self.bets = {
            'Line-1': None,
            'Line-2': None,
            'Line-3': None,
            'Diagonal-1': None,
            'Diagonal-2': None
        }
        self.bet_amount = None
        self.balance = None
        self.line_wins = {}
        self.slot_rack = slot_rack_object

        # Get initial balance from user
        while True:
            try:
                print(f"You may start with up to --{MAX_BALANCE} coins-- for a session")
                user_balance = int(input("Enter your starting balance: "))
                if 0 < user_balance <= MAX_BALANCE:
                    self.balance = user_balance
                    # print("-" * 30)
                    break
                else:
                    # print("Balance Out-of-Bounds")
                    raise ValueError
            except ValueError:
                print(">> You may have entered an Invalid Character\n>> Please enter a valid number\n")
                continue

    def get_balance(self):
        return self.balance

    def get_bets(self):
        # Initialise all line_bets to 'no'
        for line in self.bets.keys():
            self.bets[line] = 'n'

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
                # continue
            except IndexError:
                print("Please enter either 'y' or 'n'")

        while True:
            try:
                # Get bet_amount for 1 line from user
                self.bet_amount = int(input("\nHow much would you like to bet on each line: "))
                # Multipy bet_amount with total lines user has bet on and check for available balance
                total_bet_amount = self.bet_amount * count
                if 0 > total_bet_amount or total_bet_amount > self.balance:
                    raise ValueError
                self.balance -= total_bet_amount
                break
            except ValueError:
                print(">> You may have entered an Invalid Character or your total bets exceed your balance\n"
                      ">> Please enter a valid number")

        self.print_bets(count, total_bet_amount)

    def print_bets(self, line_count, total_bet):
        # Displays all the lines the user is betting function
        # And shows total bet
        print("\n>> You are betting on the following lines:")
        for line, bet in self.bets.items():
            if bet == 'y':
                print(f">> {line}")
        print(f">> You are betting {self.bet_amount} coins on {line_count} Lines\n"
              f">> Your total bet is {total_bet}")

    def check_line_wins(self):
        board_layout = self.slot_rack.get_slot_state()
        self.line_wins = {}

        # Check Line-1
        line_1_character = board_layout[0][0]
        # print(line_1_character)
        if all(char is line_1_character for char in board_layout[0]):
            self.line_wins["Line-1"] = SYMBOL_PAYOUT[line_1_character]
        # Check Line-2
        line_2_character = board_layout[1][0]
        # print(line_2_character)
        if all(char is line_2_character for char in board_layout[1]):
            self.line_wins["Line-2"] = SYMBOL_PAYOUT[line_2_character]
        # Check Line-3
        line_3_character = board_layout[2][0]
        # print(line_3_character)
        if all(char is line_3_character for char in board_layout[2]):
            self.line_wins["Line-3"] = SYMBOL_PAYOUT[line_3_character]
        # Check diagonal-1
        diagonal_1 = []
        for i in range(RACK_SIZE):
            diagonal_1.append([i, i])
        # print(diagonal_1)
        diagonal_1_character = board_layout[diagonal_1[0][0]][diagonal_1[0][1]]
        for row, col in diagonal_1[1:]:
            if board_layout[row][col] != diagonal_1_character:
                break
        else:
            self.line_wins["Diagonal-1"] = SYMBOL_PAYOUT[diagonal_1_character]
        # Check diagonal-2
        diagonal_2 = []
        for i in range(RACK_SIZE):
            diagonal_2.append([i, RACK_SIZE - 1 - (1 * i)])
        # print(diagonal_2)
        diagonal_2_character = board_layout[diagonal_2[0][0]][diagonal_2[0][1]]
        for row, col in diagonal_2[1:]:
            if board_layout[row][col] != diagonal_2_character:
                break
        else:
            self.line_wins["Diagonal-2"] = SYMBOL_PAYOUT[diagonal_2_character]

        # print(self.line_wins)
        self.print_wins()

    def print_wins(self):
        print("-" * 30)
        if not self.line_wins:
            print("You did not win on any lines")
            return
        print(">> You won on the lines:")
        for line, multiplier in self.line_wins.items():
            print(f">> {line} -> Multiplier x{multiplier}")
        self.calculate_payout()

    def calculate_payout(self):
        total_payout = 0
        for line, multiplier in self.line_wins.items():
            if self.bets[line] == 'y':
                total_payout += self.bet_amount * multiplier
        print(f">> Your total payout from this roll: {total_payout} Coins")
        self.balance += total_payout
