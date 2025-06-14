# Write your code here
import re 

def abc_or_xyz(string):
    
    match = re.fullmatch('(abc)|(xyz)', string)
    
    if match:
        return True
    else:
        return False