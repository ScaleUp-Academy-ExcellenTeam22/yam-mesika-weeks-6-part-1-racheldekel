def get_positive_numbers(list_num):
    """
    function that gets list of numbers and return the positive numbers
    :param list_num: list of numbers
    :return: list of positive numbers
    """
    return list(filter(lambda x: (x >= 0), list_num) )


if __name__ == '__main__':
    list1 = [-10, 21, 4, -45, -66, 93, -11]
    pos_nos = get_positive_numbers(list1)
    print("Positive numbers in the list: ", *pos_nos)
