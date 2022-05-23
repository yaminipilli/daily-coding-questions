"""
For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

10 = max(10, 5, 2)
7 = max(5, 2, 7)
8 = max(2, 7, 8)
8 = max(7, 8, 7)
"""

def printMax(arr, n, k):
    max = 0
    a=[]
    for i in range(n - k + 1):
        max = arr[i]
        for j in range(1, k):
            if arr[i + j] > max:
                max = arr[i + j]
        a.append(max)
    print(a)
arr = [10, 5, 2, 7, 8, 7]
n = len(arr)
k = 3
printMax(arr, n, k)
