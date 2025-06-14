def findMaximum(list):
    if len(list) == 0:
        raise IndexError("The list is empty")
    
    if len(list) == 1:
        return list[0]
    
    rest_max = findMaximum(list[1:])
    
    if list[0] > rest_max:
        return list[0]
    else:
        return rest_max
