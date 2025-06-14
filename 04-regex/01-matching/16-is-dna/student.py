# Write your code here
import re 

def is_dna(string):
    
    match = re.fullmatch('[GATC]*', string)
    
    if match:
        return True
    else:
        return False