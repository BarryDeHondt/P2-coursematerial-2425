
# Write your code here
import re 

def contains_three_digits(string):
    
    match = re.fullmatch('.*[0-9]...*', string)
    
    if match:
        return True
    else:
        return False