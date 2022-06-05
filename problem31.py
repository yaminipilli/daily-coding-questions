"""
The edit distance between two strings refers to the minimum number of character insertions, deletions, and substitutions required to change one string to the other. For example, the edit distance between “kitten” and “sitting” is three: substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.
"""

def edit_dist(str1, str2):


    if len(str1) > len(str2):
        difference = len(str1) - len(str2)
        l=len(str2)

    elif len(str2) > len(str1):
        difference = len(str2) - len(str1)
        l=len(str1)

    else:
        difference = 0

    for i in range(l):
        if str1[i] != str2[i]:
            difference += 1

    return difference

print(edit_dist( "sitting","kitten")) 
