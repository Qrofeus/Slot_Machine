from random import sample, randint
from time import sleep
from os import system

RACK_SIZE = 3

SYMBOLS = {
    'A': 4,
    'B': 3,
    'C': 2,
    'W': 1
}

SYMBOL_PAYOUT = {
    'A': 2,
    'B': 3,
    'C': 4,
    'W': 10
}


def print_winning_combinations():
    system('cls')
    print("Winning Combinations:")
    for symbol, multiplier in SYMBOL_PAYOUT.items():
        print(f"{'-'.join([symbol] * 3)} : x{multiplier} Multiplier")
    print('-' * 30)
    display_lines()
    print('-' * 30)
    input("Press 'ENTER' to continue:")


def display_lines():
    print("Slot Machine Layout:")
    print("D-1 \\")
    for row in range(RACK_SIZE):
        print(f"L-{row+1} - ", end="")
        print(" | ".join(["X"] * RACK_SIZE))
    print("D-2 /")


class SlotRack:
    def __init__(self):
        # Create 3x3 slot machine board
        self.rack = [[None for _ in range(RACK_SIZE)] for _ in range(RACK_SIZE)]
        # print(self.rack)
        rack_reel = list()
        for symbol, freq in SYMBOLS.items():
            for _ in range(freq):
                rack_reel.append(symbol)

        self.rack_1 = sample(rack_reel, len(rack_reel))
        # print(self.rack_1)
        self.rack_2 = sample(rack_reel, len(rack_reel))
        # print(self.rack_2)
        self.rack_3 = sample(rack_reel, len(rack_reel))
        # print(self.rack_3)

        print_winning_combinations()

    def roll_slots(self):
        print("-" * 30)
        print("Rolling slots ", end="")
        for _ in range(5):
            sleep(1)
            print(". ", end="")
        print()
        print("-" * 30)

        reel_size = len(self.rack_1)
        for row in range(len(self.rack)):
            start = randint(0, reel_size - 1)
            for pos in range(3):
                self.rack[row][pos] = self.rack_1[(start + pos) % reel_size]

        # Transpose Rack for vertical reels
        # Allows for bets to be counted horizontally
        for i in range(RACK_SIZE):
            for j in range(i + 1, RACK_SIZE):
                self.rack[i][j], self.rack[j][i] = self.rack[j][i], self.rack[i][j]
        # print(self.rack)

    def get_slot_state(self):
        return self.rack

    def __str__(self):
        rack_rows = [" | ".join(list(map(str, self.rack[0]))),
                     " | ".join(list(map(str, self.rack[1]))),
                     " | ".join(list(map(str, self.rack[2])))]
        display_rack = "\n--|---|--\n".join(rack_rows)
        return display_rack
