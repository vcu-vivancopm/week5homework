"""Homework file for my students to have fun with some algorithms! """


def find_greatest_number(incoming_list: list):
    """
    Required parameter, incoming_list, should be a list.
    Find the largest number in the list.
    """
    return max(incoming_list)


def find_least_number(incoming_list: list):
    """
    Required parameter, incoming_list, should be a list.
    Find the smallest/least number in the list.
    """
    return min(incoming_list)


def add_list_numbers(incoming_list: list):
    """
    Required parameter, incoming_list, should be a list.
    Add all the values together and return it.
    """
    if isinstance(incoming_list, list) == False:
        return 0
    return sum(incoming_list)


def longest_value_key(incoming_dict: dict):
    """
    Required parameter, incoming_dict, should be a dict.
    Find the KEY that has a value with the highest length, use the len() function
    """
    longest_value = max(incoming_dict.values(), key=len)

    for key, value in incoming_dict.items():
        if longest_value == value:
            longest_key = key
    print(longest_key)
