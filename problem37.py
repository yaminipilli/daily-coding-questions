"""The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.

For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

"""

def findPowerSet(S):
 
    N = int(pow(2, len(S)))
    s = set()

    for i in range(N):
        
        for j in range(len(S)):
            
            # if jth bit of i is set, print S[j]
            if i & (1 << j):
                s.add(S[j])
 
        print(s)
        s.clear()
 
 
S = [1, 2, 3]
findPowerSet(S)

