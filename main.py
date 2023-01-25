from SlotRack import SlotRack, print_winning_combinations as print_multipliers
from CoinMachine import CoinMachine
from logo_art import slot_machine_logo
from time import sleep
from os import system

if __name__ == '__main__':
    print(slot_machine_logo)
    input("Press 'ENTER' to start game:")

    slot_rack = SlotRack()
    coin_machine = CoinMachine(slot_rack)
    # print(f"Your current balance: {coin_machine.get_balance()} Coins\n")
    while True:
        # print("-" * 30)
        system('cls')
        print(f"Your current balance: {coin_machine.get_balance()} Coins\n")
        coin_machine.get_bets()
        slot_rack.roll_slots()
        print(slot_rack)
        coin_machine.check_line_wins()

        print("-" * 30)
        if coin_machine.get_balance() <= 0:
            print(">> You are out of coins...\n>> Thank You for playing")
            break
        try:
            play_again = input("Press 'ENTER' to play again\n"
                               "['q' to Quit]['m' for Multipliers]: ")[0].lower()
            if play_again == 'm':
                print_multipliers()
            elif play_again == 'q':
                break
        except IndexError:
            continue

    # print("-" * 30)
    system('cls')
    print(f"Cashing out ", end="")
    for _ in range(3):
        print(". ", end="")
        sleep(1)
    print(f"\nYou received {coin_machine.get_balance()} Coins")

