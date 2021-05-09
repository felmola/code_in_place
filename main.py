"""
TODO: Write a description here
"""
# Imports


# Constants
MAX_STONES = 20


def main():
    stones = MAX_STONES
    while stones > 0:
        print("There are", str(stones), "stones left.")
        ask_stones = ask_user_stones()
        print("User asked for", str(ask_stones), "stones.")
        stones = stones - ask_stones
        print()
    print("There are not any more stones.")


def ask_user_stones():
    ask_stones = int(input("How many stones would you like to remove?"))
    return ask_stones




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
