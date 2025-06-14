# Write your code here
import re


def equals_abc(string):
    
    match = re.fullmatch('abc', string)
    
    if match:
        return True
    else:
        return False
    
    