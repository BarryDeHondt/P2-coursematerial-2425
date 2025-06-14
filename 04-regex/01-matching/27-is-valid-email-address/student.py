# Write your code here
import re 

def is_valid_email_address(string):
    
    match = re.fullmatch(r'[a-z0-9.]+@(ucll.be|student.ucll.be)$', string)
    
    if match:
        return True
    else:
        return False