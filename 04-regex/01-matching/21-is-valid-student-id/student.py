# Write your code here
import re 

def is_valid_student_id(string):
    
    match = re.fullmatch('^([s|r, S|R])\d{7}', string)
    
    if match:
        return True
    else:
        return False