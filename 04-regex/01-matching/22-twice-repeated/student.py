# Write your code here
import re 

def twice_repeated(string):
    
    match = re.fullmatch(r'^(.)\1', string)
    
    if match:
        return True
    else:
        return False