# Write your code here
import re

def equals_a(string):
    
    match = re.fullmatch('a', string)
    
    if match:
        return True
        
    else:
        return False
        

equals_a('a')
    