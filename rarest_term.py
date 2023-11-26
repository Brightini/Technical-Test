#!/usr/bin/python3
# This script computes the nth rarest term in a list on integers


def nth_most_rate(list: list, n: int) -> int:
    """ A function that computes and returns the nth
    rarest term in a list of integers

    Args:
        list(list): a list of integers
        n(int): the nth rarest term

    Return:
        The functon returns the nth rarest items.
        Else None if the wrong value of n is passed
        or the list is empty
    """

    # Each item in the list, with their corresponding number
    # of appearances are stored in a dictionary to easily
    # compute the rarest nth term
    items_dict = {}
    for item in list:
        items_dict[item] = items_dict.get(item, 0) + 1

    items_count = len(items_dict)
    sorted_items = sorted(items_dict.items(), key=lambda x: x[1])

    if n > 0 and n <= items_count:
        nth_item = sorted_items[n-1][0]
        return nth_item
    else:
        return None

# Lists with different values can be passed here, with
# different values of n to determine the nth rarest term
result = nth_most_rate([6,6,7,7,7,7,3,3,3,3,3,0,0,0], 4)
if result is not None:
    print(result) # output: 3
else:
    print("n must be > 0 and <= the number of items in the list")
