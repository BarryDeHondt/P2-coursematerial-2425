import re


def is_valid_student_id(string):
    return re.fullmatch('[s|r]\d+0123456789', string)
