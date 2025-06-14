import re

# Write your code here
import re 

def only_letters(string):
    
    match = re.fullmatch('[a-z|A-Z]*', string)
    
    if match:
        return True
    else:
        return False