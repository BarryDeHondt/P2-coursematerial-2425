# Write your code here
import re 

def contains_no_a(string):
    
    match = re.fullmatch(r'[^a]*', string)
    
    if match:
        return True
    else:
        return False