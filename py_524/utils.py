def standard_deviation(x):
    """
    Calculates the standard deviation.
    :param x: an array of numbers
    :return: The standard deviation.
    >>> standard_error([1, 2, 3])
    0.81649658092772603
    """
    n = len(x)
    mean = sum(x) / n
    ssq = sum((x_i-mean)**2 for x_i in x)
    stdev = (ssq/n)**0.5
    return(stdev)

def standard_error(x):
    """
    Calculates the standard error.
    :param x: an array of numbers
    :return: The standard error.
    >>> standard_error([1, 2, 3])
    0.47140452079103173
    """
    return standard_deviation(x)/len(x)**0.5
