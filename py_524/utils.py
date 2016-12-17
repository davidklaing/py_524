def standard_deviation(x):
    """
    Calculates the standard deviation.
    :param x: an array of numbers
    :return: The standard deviation.
    >>> standard_error([1, 2, 3])
    1
    """
    n = len(x)
    mean = sum(x) / n
    ssq = sum((x_i - mean) ** 2 for x_i in x)
    standard_dev = (ssq / (n - 1)) ** 0.5
    return standard_dev


def standard_error(x):
    """
    Calculates the standard error.
    :param x: an array of numbers
    :return: The standard error.
    >>> standard_error([1, 2, 3])
    0.5773502691896257
    """
    return standard_deviation(x) / len(x) ** 0.5
