from random import sample, randint

RACK_SIZE = 3

SYMBOLS = {
    'A': 4,
    'B': 3,
    'C': 2,
    'W': 1
}


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

    def roll_slots(self):
        reel_size = len(self.rack_1)
        for row in range(len(self.rack)):
            start = randint(0, reel_size - 1)
            for pos in range(3):
                self.rack[row][pos] = self.rack_1[(start + pos) % reel_size]

        # print(self.rack)
        # Transpose Rack for vertical reels
        # Allows for bets to be counted horizontally
        for i in range(RACK_SIZE):
            for j in range(i + 1, RACK_SIZE):
                self.rack[i][j], self.rack[j][i] = self.rack[j][i], self.rack[i][j]

    def get_slot_state(self):
        rack_rows = [" | ".join(list(map(str, self.rack[0]))),
                     " | ".join(list(map(str, self.rack[1]))),
                     " | ".join(list(map(str, self.rack[2])))]
        display_rack = "\n--|---|--\n".join(rack_rows)
        return display_rack
