# Write your code here


import re


def equals_b(string):
    
    match = re.fullmatch('b', string)
    
    if match:
        return True
    else:
        return False