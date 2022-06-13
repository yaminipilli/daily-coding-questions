"""Given an array of integers where every integer occurs three times except for one integer, which only occurs once, find and return the non-duplicated integer.

For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.
"""
def singleNum(l):
    
    unique = list(l)
    arr_count=[]
    
    for i in unique:
        count=l.count(i)
        arr_count.append(count)
    k=arr_count.index(1)
    return unique[k]
    
l = [6, 1, 3, 3, 3, 6, 6]

print(singleNum(l))

