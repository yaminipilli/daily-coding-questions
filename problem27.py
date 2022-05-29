'''Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
'''

def BracketsBalance(expr):
    st = []
    
    for char in expr:
        if char in ["(", "{", "["]:
            st.append(char)
        else:
            current_char = st.pop()
            if current_char == '(':
                if char != ")":
                    return False
            if current_char == '{':
                if char != "}":
                    return False
            if current_char == '[':
                if char != "]":
                    return False
 
    if st:
        return False
    return True
 
 
exp = "([])[]({})"
 
print(BracketsBalance(exp))
    
