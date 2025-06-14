# Write your code here
import re 

def ababa(string):
    
    match = re.fullmatch(r'(.+?)(.+?)\1\2\1', string)
    
    if match:
        return True
    else:
        return False