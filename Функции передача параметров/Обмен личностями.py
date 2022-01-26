def swap(first, second):
    temp = first[:]
    first.clear()
    first.extend(second)
    second.clear()
    second.extend(temp)
    
