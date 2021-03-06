"""Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5."""



def findMaxSum(arr, n):
    incl = 0
    excl = 0  
    for i in arr:
       
        new_excl = max (excl, incl)
        
        incl = excl + i
        excl = new_excl
   
    return max(excl, incl)
 
if __name__ == "__main__":
    arr = [5, 5, 10, 100, 10, 5]
    N = 6
     
   
    print (findMaxSum(arr, N))
 
