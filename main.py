"""
TODO: Write a description here
"""
# Imports


# Constants
MAX_STONES = 20


def main():
    stones = MAX_STONES
    round = 0
    while stones > 0:
        print("There are", str(stones), "stones left.")
        round += 1
        player = define_player(round)
        ask_stones = ask_user_stones()
        stones = stones - ask_stones
        print()
    print("There are not any more stones.")


def ask_user_stones():
    ask_stones = int(input("How many stones would you like to remove?"))
    print("User asked for", str(ask_stones), "stones.")
    return ask_stones

def define_player(round):
    player = None
    if round % 2 == 0:
        player = 0
        print("Round is", str(round))
        print("Player is", str(player))
        return player
    else:
        player = 1
        print("Round is", str(round))
        print("Player is", str(player))
        return player

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
