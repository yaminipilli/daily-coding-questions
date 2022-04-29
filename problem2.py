'''Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

solution:'''

def productArray(arr, n):
 
    if(n == 1):
        print(0)
        return
         
    left = [0]*n
    right = [0]*n
 
    prod = [0]*n
 

    left[0] = 1
 

    right[n - 1] = 1
 
    for i in range(1, n):
        left[i] = arr[i - 1] * left[i - 1]
 
    for j in range(n-2, -1, -1):
        right[j] = arr[j + 1] * right[j + 1]

    for i in range(n):
        prod[i] = left[i] * right[i]
 
    for i in range(n):
        print(prod[i], end =' ')
 
 
arr = [10, 3, 5, 6, 2]
n = len(arr)
print("The product array is:")
productArray(arr, n)
