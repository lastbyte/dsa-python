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
