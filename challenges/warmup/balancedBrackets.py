'''
Given a string of three types of brackets (), {}, and []
Determine if the string is balanced, i.e.
- There are no unmatched brackets
- The subset of brackets within the confines of a matched pair of brackets
 is also balanced.
'''


def isBalanced(s):
    # Traverse only once, no recursion
    # Keep track of unclosed brackets.
    unclosed = {
        '{': 0,
        '[':0,
        '(':0,
    }
    match = {
        ']':'[',
        ')':'(',
        '}':'{'
    }

    stack = [s[0]]

    for c in s:
        if c not in unclosed:
            # is closing character
            last_opened = stack.pop()
            if match[c] != last_opened:
                return "NO"
            
            unclosed[match[c]] -= 1
            if unclosed[match[c]] < 0:
                return "NO"
        else:
            # is opening character
            stack.append(c)
            unclosed[c] += 1
    
    for count in unclosed.values():
        if count != 0:
            return "NO"
    
    return "YES"
## FAILS ON INPUT:    {[(])} returns YES instead of NO

