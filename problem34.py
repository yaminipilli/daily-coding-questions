""" given the string "race", you should return "ecarace", since we can add three letters to it (which is the smallest amount to make a palindrome). There are seven other palindromes that can be made from "race" by adding three letters, but "ecarace" comes first alphabetically.

As another example, given the string "google", you should return "elgoogle".

"""

def is_palindrome(s):
    return s[::-1] == s


def get_palindrome(s):

    if is_palindrome(s):
        return s

    if s[0] == s[-1]:
        return s[0] + get_palindrome(s[1:-1]) + s[-1]
    else:
        pal1 = s[0] + get_palindrome(s[1:]) + s[0]
        pal2 = s[-1] + get_palindrome(s[:-1]) + s[-1]
        
        if len(pal1) > len(pal2):
            return pal2
        elif len(pal1) < len(pal2):
            return pal1

        return pal1 if pal1 < pal2 else pal2


print(get_palindrome("race"))
print(get_palindrome("google"))
