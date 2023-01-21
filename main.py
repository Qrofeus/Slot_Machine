from SlotRack import SlotRack
from CoinMachine import CoinMachine

if __name__ == '__main__':
    slot_rack = SlotRack()
    coin_machine = CoinMachine()

    print(f"Your current balance: {coin_machine.get_balance()} Coins")
    coin_machine.get_bets()

    slot_rack.roll_slots()
    print(slot_rack.get_slot_state())

    # coin_machine.calculate_payout(slot_rack)

