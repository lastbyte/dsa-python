'''
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
 

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
 

Constraints:

0 <= word1.length, word2.length <= 500
word1 and word2 consist of lowercase English letters.

link -> https://leetcode.com/problems/edit-distance/

'''

from typing import List


class Solution:
    def edit_distance(self, word1: str, word2: str) -> int:
        memory = [[float('inf')] * (len(word1) + 1) for i in range(len(word2) + 1)]
        for i in range(len(word1) + 1):
            memory[0][i] = i
        for j in range(len(word2) + 1):
            memory[j][0] = j
        i = 1
        j = 1
        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    memory[j][i] = memory[j - 1][i - 1]
                else:
                    memory[j][i] = 1 + min(memory[j - 1][i - 1], memory[j][i - 1], memory[j - 1][i])

        return memory[len(word2)][len(word1)]


if __name__ == "__main__":
    solution = Solution()
    result = solution.edit_distance("intention", "execution")
    print(result)
