"""
Implements the game of Rock-Paper-Scissors!

History:
This classic game dates back to the Han Dinesty, over 2200 years ago.
The First International Rock-Paper-Scissors Programming Competition
was held in 1999 and was won by a team called "Iocaine Powder"

The Game:
Each player choses a move (simultaneously) from the choices:
rock, paper or scissors.
If they chose the same move the game is a tie. Otherwise:
rock beats scissors
scissors beats paper
paper beats rock.

In this program a human plays against an AI. The AI choses randomly
(we promise). The game is repeated N_GAMES times and the human gets
a total score. Each win is worth +1 points, each loss is worth -1
"""
#todo: Create input for human

# Imports
import random

# Constants

def main():
    ask_user()
    ask_machine()


def ask_user():
    user_decision = int(input("Please choose a move from Rock(1), Paper(2), or Scissors(3): "))
    print("User input was:", str(user_decision))
    return user_decision


def ask_machine():
    machine_decision = random.randint(1, 3)
    print("Machine input was: ", str(machine_decision))
    return machine_decision


if __name__ == '__main__':
    main()