def full_names(first_names_list, last_names_list, min_length=None):
    """
    function that gets list of first name and list for last name and combination them together
    :param first_names_list: list of first name
    :param last_names_list: list for last name
    :param min_length: minimum length
    :return: list of the combination
    """
    full_names_list = [first_name.title() + " " + last_name.title()
                       for first_name in first_names_list
                       for last_name in last_names_list]

    if not min_length:
        return full_names_list

    return list(filter(lambda name: len(name) >= min_length, full_names_list))


if __name__ == '__main__':
    first_names = ['avi', 'moshe', 'yaakov']
    last_names = ['cohen', 'levi', 'mizrahi']
    print(full_names(first_names, last_names, 10))
    print(full_names(first_names, last_names))
