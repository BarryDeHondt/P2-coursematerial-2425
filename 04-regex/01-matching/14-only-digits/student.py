# Write your code here
import re 

def only_digits(string):
    
    match = re.fullmatch('[0123456789]*', string)
    
    if match:
        return True
    else:
        return False