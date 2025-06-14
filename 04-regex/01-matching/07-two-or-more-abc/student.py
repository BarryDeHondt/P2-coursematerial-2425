# Write your code here
import re

def two_or_more_abc(string):
    
    match = re.fullmatch('(abc)+(abc)+', string)
    
    if match:
        return True
    else:
        return False