# Write your code here
import re 

def is_number(string):
    
    match = re.fullmatch('\d+(\.\d+)?', string)
    
    if match:
        return True
    else:
        return False