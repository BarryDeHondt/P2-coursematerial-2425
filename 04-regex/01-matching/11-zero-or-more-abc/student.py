# Write your code here
import re

def zero_or_more_abc(string):
    
    match = re.fullmatch('(abc)*', string)
    
    if match:
        return True
    else:
        return False