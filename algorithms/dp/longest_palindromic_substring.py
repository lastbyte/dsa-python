'''
Given a string s, return the longest palindromic substring in s.
'''
from pprint import pprint


class Solution:
    def longestPalindrome(self, s: str) -> str:
        memory = [[False] * len(s) for i in range(len(s) + 1)]
        return self.longestPalindromeUtil(s, memory)


    def longestPalindromeUtil(self, s: str, memory):
        length = len(s)
        #initialize all substring of length 1 and 0 to palindrome in memory
        for i in range(length):
            memory[1][i],memory[0][i] = True,True
            max_len = 1
            palindrome = s[i:i + 1]

        for i in range(length-1):
            if s[i] == s[i+1]:
                memory[2][i] = True
                max_len = 2
                palindrome = s[i:i+2]

        for i in range(3, length + 1):
            for j in range(length + 1 - i):
                memory[i][j] = True if memory[i-2][j+1] is True and s[j] == s[j+i-1] else False
                if memory[i][j] is True and i > max_len:
                    max_len = i
                    palindrome = s[j:j+i]
        return palindrome





'''
driver code
'''
if __name__ == "__main__" :

    solution = Solution()
    result = solution.longestPalindrome('babad')
    print(result)
    result = solution.longestPalindrome('cbbd')
    print(result)
    result = solution.longestPalindrome("aacabdkacaa")
    print(result)
    result = solution.longestPalindrome("ccc")
    print(result)
