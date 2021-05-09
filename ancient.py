"""
This is the Ancient Game of Nim. There is an initial pile of stones. Players take turns to take 1 or 2 stones from the
pile. The one that has the last turn before the stones runs out, wins the game.
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


def define_player(round):
    """
    This function assigns a player role depending if the round is even or odd.
    :param round: comes predefined in main().
    :return: returns a variable player as an even (0) or odd (1) number.
    """
    player = None
    if round % 2 == 0:
        player = 0
        #print("Round is", str(round))
        #print("Player is", str(player))
        return player
    else:
        player = 1
        #print("Round is", str(round))
        #print("Player is", str(player))
        return player


def ask_user_stones(player):
    """
    Takes the value of player (an even or odd number) and returns an input message for that player asking for the number
    of stones to take.
    :param player: An even or off number from define_player().
    :return: The number of stones the player has decided to take.
    """
    if player == 0:
        ask_stones = int(input("Player 2 would you like to remove 1 or 2 stones?"))
        while not (ask_stones == 1 or ask_stones == 2):
            ask_stones = int(input("Please enter 1 or 2: "))
    else:
        ask_stones = int(input("Player 1 would you like to remove 1 or 2 stones?"))
        while not (ask_stones == 1 or ask_stones == 2):
            ask_stones = int(input("Please enter 1 or 2: "))
    #print("Player", str(player), "removed", str(ask_stones), "stones.")
    return ask_stones


def final_statement(player):
    """
    After there are not any more stones, depending on the player, describes who won the game.
    :param player: From define_player()
    :return: An statement of which player won the game.
    """
    if player == 0:
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
