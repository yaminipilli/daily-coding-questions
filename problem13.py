"""Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".

solution:
"""

def Substringlen(str, k):
    start, end = 0, k
    max_len = k
    l=len(str)
    while end <= l:
        
        if len(set(str[start:end])) <= k:
            
            current_len = end - start
            if current_len >= max_len:
                max_len = current_len
        
            end += 1
        else:
            start += 1
    return max_len

print(Substringlen("abcba", 2))

