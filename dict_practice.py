"""
This program...
"""

# Installs:


# Imports:


# Constants:

def main():

    # Defining a dictionary:
    dict = {"color_1": "yellow",
            "color_2": "blue",
            "color_3": "red"}

    # Accessing a value of a dictionary using a key:
    print(dict["color_1"])

    # Setting a value to a key of an existing dictionary:
    dict["color_4"] = "black"
    print(dict["color_4"])

    # Can modify an existing value like a regular variable:
    dict["stripes"] = 3
    print(dict["stripes"])
    dict["stripes"] = dict["stripes"] + 1
    print(dict["stripes"])

    # Can assing a value from a dictionary to a variable:
    stripe_color_1 = dict["color_1"]
    print(stripe_color_1)

    # Can not call non-existing values from non-existing keys.

    # Can check for membership in a dictionary:
    if "color_1" in dict:
        print("Yep")
    else:
        print("Nop")

    # Can check for no membership in a dictionary:
    if "color_1" not in dict:
        print("Nop")
    else:
        print("Yep")



if __name__ == "__main__":
    main()