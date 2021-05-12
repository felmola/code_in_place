def main():
    print("Enter a sequence of non-decreasing numbers.")
    user_input = float(input("Enter num: "))
    prev_user_input = user_input - 1
    seq_lenght = 0
    while user_input >= prev_user_input:
        seq_lenght = seq_lenght + 1
        prev_user_input = user_input
        user_input = float(input("Enter num: "))
    print("Thanks for playing!")
    print("Sequence lenght: ", str(seq_lenght))


if __name__ == "__main__":
    main()