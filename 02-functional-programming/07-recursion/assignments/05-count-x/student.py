def countX(text):
    if not text:
        return 0
    if text[0] == 'x':
        return 1 + countX(text[1:])
    return countX(text[1:])
        
         
        
    
    