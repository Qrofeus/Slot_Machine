from SlotRack import SlotRack
from CoinMachine import CoinMachine
from time import sleep

if __name__ == '__main__':
    slot_rack = SlotRack()
    coin_machine = CoinMachine(slot_rack)

    # print(f"Your current balance: {coin_machine.get_balance()} Coins\n")
    while True:
        print("-" * 30)
        coin_machine.get_bets()

        slot_rack.roll_slots()
        # print(slot_rack.get_slot_state())
        print(slot_rack)

        coin_machine.check_line_wins()

        print("-" * 30)
        print(f"Your current balance: {coin_machine.get_balance()} Coins\n")
        if coin_machine.get_balance() <= 0:
            print(">> You are out of coins...\n>> Thank You for playing")
            break

        try:
            play_again = input("Press 'ENTER' to play again ['q' to quit]: ")
            if play_again[0].lower() == 'q':
                break
        except IndexError:
            continue

    print("-" * 30)
    print(f"Cashing out ", end="")
    for _ in range(3):
        print(". ", end="")
    print(f"\nYou received {coin_machine.get_balance()} Coins")

