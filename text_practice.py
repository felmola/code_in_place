"""
### Reverse String
def main():
    str = "Carajo!"
    print(str)
    str = reverse_string_simple(str)
    print(str)

def reverse_string(str):
    reverse = ""
    for i in range(len(str)):
        ch = str[i]
        # print(ch)
        reverse = ch + reverse

    return reverse


def reverse_string_simple(str):
    reverse = ""
    for ch in str:
        reverse = ch + reverse

    return reverse
"""
###

import random

N_LABELS = 5000


def main():
    for i in range(N_LABELS):
        random_part = pad(random.randint(0, N_LABELS), 5)
        consecutive_part = pad(i, 4)
        code = random_part + consecutive_part
        print(code)


def pad(num, length):
    num_string = str(num)
    while len(num_string) < length:
        num_string = "0" + num_string

    return num_string


if __name__ == '__main__':
    main()