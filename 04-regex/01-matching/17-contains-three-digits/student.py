import re 


def contains_three_digits(string):
    return re.fullmatch('[0123456789]...*', string)