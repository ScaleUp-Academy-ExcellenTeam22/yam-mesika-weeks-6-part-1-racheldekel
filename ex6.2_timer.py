import time


def timer(f, *args, **kwargs):
    """
    function that gets parameters and calculate the time that takes for it.
    :param f: function
    :param args: pointer to item
    :param kwargs: dictionary
    :return:
    """
    start_time = time.time()
    f(*args, **kwargs)
    end_time = time.time()
    time_takes = end_time - start_time
    return time_takes


if __name__ == '__main__':
    print(timer(print, "Hello"))
    print(timer(zip, [1, 2, 3], [4, 5, 6]))
    print(timer("Hi {name}".format, name="Bug"))
