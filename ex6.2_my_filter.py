def my_filter(function, iterable):
    """
    generator function that checks if the item with the function gets true
    :param function: function to check on
    :param iterable: the value to send the function with
    :return: if true - return the item (with yield)
    """
    for item in iterable:
        if function(item):
            yield item


def is_mature(age):
    """
    bool function that check if the person is adult (as exmple for function)
    :param age:
    :return:
    """
    return age >= 18


if __name__ == '__main__':
    ages = [0, 1, 4, 10, 20, 35, 56, 84, 120]
    mature_ages = filter(is_mature, ages)
    our_generator = my_filter(is_mature, ages)
    print(tuple(mature_ages))
    print(tuple(our_generator))
