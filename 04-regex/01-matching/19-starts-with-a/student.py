# Write your code here
import re 

def starts_with_a(string):
    
    match = re.match('a', string)
    
    if match:
        return True
    else:
        return False