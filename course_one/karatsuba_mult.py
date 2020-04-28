""" Implementation of generalized Karatsuba integer multiplication. """


def multiply(x, y):
    """
    Given two integers of any length, calculate the product using the recursive Karatsuba algorithm.

    :param x: the first integer
    :param y: the second integer
    :return: the product of the two inputs
    """
    if x in [0, ""] or y in [0, ""]:
        return 0

    # Determine the sign of the product.
    # While doing this, remove the negative symbol. We don't want to include this when splitting a number.
    x_str, y_str = str(x), str(y)
    x_int, y_int = int(x), int(y)

    sign = 1
    if x_str[0] == "-":
        x_str = x_str[1:]
        sign *= -1
    if y_str[0] == "-":
        y_str = y_str[1:]
        sign *= -1

    # Get the number of digits only after removing any negative signs.
    x_digits, y_digits = len(x_str), len(y_str)

    # Base case of two single digit numbers
    if x_digits == 1 and y_digits == 1:
        return x_int * y_int

    x_mid = x_digits // 2
    y_mid = y_digits // 2

    # Split each input in roughly half.
    a, b = x_str[:x_mid], x_str[x_mid:]
    c, d = y_str[:y_mid], y_str[y_mid:]

    # The length of the smaller split is the power the larger number is raised to.
    x_pow = len(b)
    y_pow = len(d)

    # We don't convert the inputs from str to int, since we would lose leading zeros.
    # Instead, pass the str value. Capture the number of places before converting to int.
    ac = sign * multiply(a, c)
    ad = sign * multiply(a, d)
    bc = sign * multiply(b, c)
    bd = sign * multiply(b, d)
    return 10**(x_pow + y_pow) * ac + 10**x_pow * ad + 10**y_pow * bc + bd
