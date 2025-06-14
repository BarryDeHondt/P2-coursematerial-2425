# Write your code here
import re

def three_to_ten_times_abc(string):
    
    match = re.fullmatch('(abc){3,10}', string)
    
    if match:
        return True
    else:
        return False