def get_letters(letter_a, letter_z):
    """
    function that return the letter between a - z
    :param letter_a: the start letter
    :param letter_z: the end letter
    :return: all the letters between
    """
    return [chr(i) for i in range(ord(letter_a), ord(letter_z) + 1)]


if __name__ == '__main__':
    print(get_letters('a', 'z'))
    print(get_letters('A', 'Z'))
