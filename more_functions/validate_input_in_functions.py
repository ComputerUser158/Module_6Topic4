"""
Author: Rawley Collins
Program: validate_input_in_functions.py


prompts user for name and score, prints values to console.
"""


def score_input(test_name, test_score = 0, invalid_message = 'Invalid test score, try again!'):
    """
    function that accepts params and returns a string....
    :param test_name: the name of a test/exam
    :rtype test_name: String
    :param test_score: A value between 0 and 100 representing a test score
    :rtype test_score: int
    :param invalid_message: Message displayed when an invalid score is provided.
    :rtype invalid_message: String
    :return: formatted string with test name and test score.
    :rtype: String
    """
    try:
        if 0 <= test_score <= 100:
            # print("{}: {}".format(test_name, test_score))
            return "{}: {}".format(test_name, test_score)
        else:
            return invalid_message
    except TypeError:
        raise TypeError


if __name__ == '__main__':
    try:
        print(score_input("test1", "45"))
    except TypeError:
        print("not a valid score.")