def fizzbuzz():
    current = 1
    while True:
        if current % 5 == 0 and current % 3 == 0:
            yield "fizzbuzz"
        elif current % 5 == 0:
            yield "buzz"    
        elif current % 3 == 0:
            yield "fizz"   
        else:
            yield str(current)
        current += 1
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # result = ''
        # if current % 3 == 0:
        #     result += "fizz"
        # elif current % 5 == 0:
        #     result += "buzz"
        # elif current % 5 == 0 and 3 == 0:
        #     result += "fizzbuzz"
        # else:
        #     result += str(current)
        # yield result
        # current += 1
            
        
