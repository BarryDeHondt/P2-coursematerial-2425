# Write your code here
import re 

def only_vowels(string):
    
    match = re.fullmatch('(a|e|i|o|u)*', string)
    
    if match:
        return True
    else:
        return False