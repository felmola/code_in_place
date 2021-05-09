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
        ask_stones = ask_user_stones(player)
        stones = stones - ask_stones
        print()
    final_statement(player)


def ask_user_stones(player):
    if player == 0:
        ask_stones = int(input("Player 2 would you like to remove 1 or 2 stones?"))
        while not (ask_stones == 1 or ask_stones == 2):
            ask_stones = int(input("Please enter 1 or 2: "))
    else:
        ask_stones = int(input("Player 1 would you like to remove 1 or 2 stones?"))
        while not (ask_stones == 1 or ask_stones == 2):
            ask_stones = int(input("Please enter 1 or 2: "))
    print("Player", str(player), "removed", str(ask_stones), "stones.")
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


def final_statement(player):
    if player == 0:
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
