class Solution:
    def longest_valid_parenthesis(self, s):
        if len(s) == 0:
            return 0
        memory = []
        longest_length = 0
        valid_length = 0
        for c in s:
            if c == '(':
                if len(memory) == 0:
                    valid_length = 0
                    
            if c == ')'

        return longest_length


result = Solution().longest_valid_parenthesis("))))()))))(()(())())")
print(result)

result = Solution().longest_valid_parenthesis(")()())")
print(result)
