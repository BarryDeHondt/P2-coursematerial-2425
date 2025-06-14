# Write your code here
import re

def scrape_email_addresses(string):
    
    
    pattern = r'\b[a-zA-Z0-9.]+@[a-zA-Z0-9]+(?:\.[a-zA-Z0-9]+)+\b'
    
    return re.findall(pattern, string)