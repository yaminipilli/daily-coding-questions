'''Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated successive characters as a single count and character. For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".'''


def alpha_count(s):
    c = 1               
    next = s[0]                 
    for i in range(1, len(s)):  
        if next == s[i]:        
            c += 1              
        else:               
            print(c, next, sep='', end='')  
            c=1                 
            next = s[i]     

str="AAAABBCCCAA"
print(alpha_count(str))  
