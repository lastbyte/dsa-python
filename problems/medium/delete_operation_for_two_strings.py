'''
Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.

In one step, you can delete exactly one character in either string.

 

Example 1:

Input: word1 = "sea", word2 = "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
Example 2:

Input: word1 = "leetcode", word2 = "etco"
Output: 4
 

Constraints:

1 <= word1.length, word2.length <= 500
word1 and word2 consist of only lowercase English letters.

link -> https://leetcode.com/problems/delete-operation-for-two-strings/

'''




class Solution:

    def min_distance(self, word1, word2):
        distance_memory = [[float('inf')] * (len(word2) + 1 ) for i in range(len(word1)+1)]
        return self.min_distance_util(word1, word2, distance_memory);


    def min_distance_util(self, word1,word2, distance_memory):
        
        #initailize memory

        distance_memory[0][0] = 0
        for w1 in range(1, len(word1) + 1) : distance_memory[w1][0] = w1
        for w2 in range(1, len(word2) + 1) : distance_memory[0][w2] = w2

        for w1 in range(1, len(word1)+1):
            for w2 in range(1, len(word2) + 1):
                if word1[w1-1] == word2[w2-1]:
                    distance_memory[w1][w2] = distance_memory[w1-1][w2-1]
                else:
                    distance_memory[w1][w2] = min(distance_memory[w1-1][w2], distance_memory[w1][w2-1]) + 1

        return distance_memory[len(word1)][len(word2)]

if __name__ == "__main__":
    result = Solution().min_distance(word1="leetcode", word2="etco")
    print(result)

