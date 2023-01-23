
# Console Slot Machine

A 3 reel slot machine with 5 available betting options to be run on a console/terminal built using Python

## Play the Game

Clone the project

```bash
  git clone https://github.com/Qrofeus/Slot_Machine
```

Go to the project directory

```bash
  cd Slot_Machine
```

Run main.py file using Python

```bash
  python main.py
```


## Demo

![Console run displaying "Winning Combinations" and "Machine Layout"](https://github.com/Qrofeus/Slot_Machine/blob/master/Slot_Machine_demo_01.JPG)

![Console run displaying "User bets", "Rolled Slots" and winnings](https://github.com/Qrofeus/Slot_Machine/blob/master/Slot_Machine_demo_02.JPG)
## Changing Reel Contents and Winning Multipliers

In the project directory, open **SlotRack.py** file using any text editor. 
Modify the following dictionaries to your liking.

Make sure to follow the syntax rules and match the symbols in both the dictionaries.

SYMBOLS dict -> 'symbol': Frequency  
SYMBOL_PAYOUT -> 'symbol': Multiplier
```python
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
```