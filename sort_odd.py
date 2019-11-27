def sort_array(source_array):
    odds = sorted((x for x in source_array if x%2 != 0), reverse=True)
    return [x if x%2==0 else odds.pop() for x in source_array]
    
    
'''    oddarr = []
    for e in source_array:
        if e%2 != 0:
            oddarr.append(e)
    oddarr.sort()    
    print(oddarr)
    for i in range(len(source_array)):
        if source_array[i]%2 != 0:
           source_array[i] = oddarr[0]
           oddarr.remove(source_array[i])
    return source_array
'''    

    
print(sort_array([5, 3, 2, 8, 1, 4]))

"""
You have an array of numbers.
Your task is to sort ascending odd numbers but even numbers must be on their places.

Zero isn't an odd number and you don't need to move it. If you have an empty array, you need to return it.

Example

sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]

"""
