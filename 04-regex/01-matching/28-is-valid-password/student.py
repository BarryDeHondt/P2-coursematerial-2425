# Write your code here
import re
from collections import Counter

def is_valid_password(string):
    if len(string) < 12:
        return False
    if not re.search(r'\d', string):  # At least one digit
        return False
    if not re.search(r'[a-z]', string):  # At least one lowercase letter
        return False
    if not re.search(r'[A-Z]', string):  # At least one uppercase letter
        return False
    if not re.search(r'[+\-*/.@]', string):  # At least one special character
        return False
    if re.search(r'(.)\1\1', string):  # Three of the same character in a row
        return False
    counts = Counter(string)
    if any(count >= 4 for count in counts.values()):  # Any char repeated 4+ times
        return False
    return True