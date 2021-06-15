'''
62. Unique Paths

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?



Example 1:


Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
Example 3:

Input: m = 7, n = 3
Output: 28
Example 4:

Input: m = 3, n = 3
Output: 6

link -> https://leetcode.com/problems/unique-paths/

'''
class Solution:
    def unique_paths(self,m,n):
        mem = [[-1]*n for i in range(m)]
        return self.unique_paths_util(m,n,mem)
    
    def unique_paths_util(self,m,n,mem):
        if m < 1 or n < 1:
            return 0
        if mem[m-1][n-1] != -1:
            return mem[m-1][n-1]
        if m == 1 and n == 1:
            mem[m-1][n-1] = 1;
            return mem[m-1][n-1]
        
        mem[m-1][n-1] = self.unique_paths_util(m-1, n, mem) + self.unique_paths_util(m, n-1, mem)
        return mem[m-1][n-1]


if __name__ =="__main__":
    solution = Solution()
    result = solution.unique_paths(23,12)
    print(result)
