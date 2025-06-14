# Write your code here
import re

def ten_times_abc(string):
    
    match = re.fullmatch('(abc){10}', string)
    
    if match:
        return True
    else:
        return False