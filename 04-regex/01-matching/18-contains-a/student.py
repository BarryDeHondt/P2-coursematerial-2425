# Write your code here
import re 

def contains_a(string):
    
    match = re.search('a', string)
    
    if match:
        return True
    else:
        return False