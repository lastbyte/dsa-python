'''
Given a string s, return the longest palindromic substring in s.
'''
from pprint import pprint


class Solution:
    def longestPalindrome(self, s: str) -> str:
        memory = create_array_2d(rows=len(s)+1, cols=len(s),default_value=False)
        return self.longestPalindromeUtil(s, memory)


    def longestPalindromeUtil(self, s: str, memory):
        length = len(s)
        #initialize all substring of length 1 and 0 to palindrome in memory
        for i in range(length):
            memory[1][i],memory[0][i] = True,True
            max_len = 1
            palindrome = s[i:i + 1]

        for i in range(2, length + 1):
            for j in range(length + 1 - i):
                memory[i][j] = True if memory[i-2][j+1] is True and s[j] == s[j+i-1] else False
                if memory[i][j] is True and i > max_len:
                    max_len = i
                    palindrome = s[j:j+i]
        return palindrome


def create_array_2d(rows,cols, default_value=None):
    return [[default_value] * cols for i in range(rows)]


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
