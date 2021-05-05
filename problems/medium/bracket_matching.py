```
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''

def bracket_matching(s: str) -> bool:
    if s is None or s == '':
        return True

    memory = []

    for i in range(0, len(s)):
        if s[i] == '(' or s[i] == '{' or s[i] == '[' :
            memory.append(s[i])
        if s[i] == ')':
            top_elem = memory.pop()
            if top_elem == '(':
                continue
            else:
                return False
        if s[i] == '}':
            top_elem = memory.pop()
            if top_elem == '{':
                continue
            else:
                return False
        if s[i] == ']':
            top_elem = memory.pop()
            if top_elem == '[':
                continue
            else:
                return False

    return True if len(memory) == 0 else False

print("(]) : " +str(bracket_matching("(])")))
print("([]) : " + str(bracket_matching("([])")))
print("( : " + str(bracket_matching("(")))
print("({([][]{})}) : " + str(bracket_matching("({([][]{})})")))
