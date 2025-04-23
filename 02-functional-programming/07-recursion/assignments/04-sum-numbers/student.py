def sum_numbers(number):
    number = abs(number)
    if number <= 9:
        return number
    
    last_digit = number % 10
    rest = number // 10
    return last_digit + sum_numbers(rest) 
        
        
        