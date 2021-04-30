
def longest_palindromic_substring(s :str) -> str :

    # initialize a memory to store the length
    row = len(s) + 1
    col = len(s) + 1
    memory = [[False] * row ] * col

    ret_string_length = 0
    ret_string = ''

    # all the substring of length 1 is a palindrome
    for i in range(0, len(s)) :
        memory[1][i] = True
        ret_string_length = 1
        ret_string = str(s[i])

    # palindrome of length 2
    for i in range(0, len(s)-1) :
        if s[i] == s[i+1] :
            memory[2][i] = True
            ret_string_length = 2
            ret_string = str(s[i:i+2])

    # for palindrome of length >= 3

    for i in range(3, len(s) + 1) :
        for j in range(0, len(s) + 1 - i):
            if s[j] == s[j+i-1] and memory[i-2][j+1] :
                memory[i][j] = True
                if ret_string_length < i:
                    ret_string_length = i
                    ret_string = str(s[j:j + i])

    return ret_string


print(longest_palindromic_substring('aacabdkacaa'))
