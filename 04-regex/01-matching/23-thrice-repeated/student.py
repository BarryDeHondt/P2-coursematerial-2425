# Write your code here
import re 

def thrice_repeated(string):
    
    match = re.fullmatch(r'^(.)\2', string)
    
    if match:
        return True
    else:
        return False