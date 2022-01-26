def mirror(arr): 
    for i in range(len(arr) - 1, -1, -1):
        arr.append(arr[i])
