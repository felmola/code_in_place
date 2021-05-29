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

    """
    Some properties fo dictionaries:
    Keys are immutable: e.g. int, float, string.
    Keys can not be changed. You need to remove the key/value pair to edit it again.
    Values can be mutable or immutable types. E.g. int, float, string, lists, dicts.
    Dictionaries are mutable: Changes made to a dictionary in a fucntion persist after the fucntion is done.
    """

    # How to return a value from a dictionary using a key?
    returned_value = dict.get("color_1") #returns None when the key does not exist or its value is None.
    print(returned_value)
    # Can return a default value if the key does not exist.
    returned_value = dict.get("color_9", "Non-existent, pal")  # returns None when the key does not exist or its value is None.
    print(returned_value)

    # Can use for loops in a dictionary looping through keys:
    for key in dict.keys(): #where xxx.keys() is like a range()
        print(str(key) + " -> " + str(dict[key]))

    # Can create a list of all keys in a dictionary:
    list_of_keys = list(dict.keys())
    print(list_of_keys)

    # Can range() over values as well.

    # Can remove elements from a dictionary:
    print(dict)
    popped_value = dict.pop("color_1") # Returns the valeu corresponding to that key.
    print(dict)
    print(popped_value)

    # Can clear the dictionary:
    dict.clear()
    print(dict)

    # Can return the length of the dictionary (the number of pairs):
    dict = {"color_1": "yellow",
            "color_2": "blue",
            "color_3": "red"}


    lenght_of_dict = len(dict)
    print(lenght_of_dict)

    # Can delete a pair, like pop but without return:
    del dict["color_1"]
    print(dict)


if __name__ == "__main__":
    main()