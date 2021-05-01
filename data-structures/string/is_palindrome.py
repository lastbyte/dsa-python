def is_palindrome(s):
    formatted_string = ''.join(c for c in s if c.isalnum()).lower()
    print(formatted_string)
    itr = 0
    while itr < len(formatted_string)//2 :
        if formatted_string[itr] != formatted_string[len(formatted_string)-itr-1]:
            return False
        itr +=1
    return True


def is_palindrome_1(s):
    left,right = 0, len(s) - 1
    while left < right:
        if s[left].isalnum():
            if s[right].isalnum():
                if s[left].lower() != s[right].lower():
                    return False
                left +=1
                right -=1
            else:
                right -=1
        else:
            left +=1
    return True

#print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome_1("A man, a plan, a canal: Panama"))