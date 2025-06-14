# Write your code here
import re

def one_or_more_b(string):
    
    match = re.fullmatch('b+', string)
    
    if match:
        return True
    else:
        return False