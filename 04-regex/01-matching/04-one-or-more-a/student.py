# Write your code here
import re


def one_or_more_a(string):
    
    match = re.fullmatch('a+', string)
    
    if match:
        return True
    else:
        return False
    
    