"""
Author: Rawley Collins
Program: string_functions.py


program: contains a function that takes a string message and returns it a specified number of times.
"""


def multiply_string(message, n):
    """multiplies a string.

    function prints a message a certain number of times
    only if the requested number of times is between 2 and 7

    :param message: the string to be multiplied
    :type message: str
    :return: message
    :rtype: str"""

    if 7 > n > 2:
        message = message * n
        return message
    else:
        print("your number of iterations was not between 7 and 2")


