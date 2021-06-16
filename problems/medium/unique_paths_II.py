'''
63. Unique Paths II
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and space is marked as 1 and 0 respectively in the grid.



Example 1:


Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
Example 2:


Input: obstacleGrid = [[0,1],[0,0]]
Output: 1

link -> https://leetcode.com/problems/unique-paths-ii/
'''
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        mem = [[-1] * len(obstacleGrid[0]) for i in range(len(obstacleGrid))]
        return self.unique_paths_util(obstacleGrid, len(obstacleGrid), len(obstacleGrid[0]), mem)

    def unique_paths_util(self, obstacleGrid, m, n, mem):
        if m < 1 or n < 1:
            return 0
        if obstacleGrid[m - 1][n - 1] == 1:
            mem[m - 1][n - 1] = 0
            return mem[m - 1][n - 1]
        if mem[m - 1][n - 1] != -1:
            return mem[m - 1][n - 1]
        if m == 1 and n == 1:
            mem[m - 1][n - 1] = 1
            return mem[m - 1][n - 1]
        mem[m - 1][n - 1] = self.unique_paths_util(obstacleGrid, m - 1, n, mem) + self.unique_paths_util(obstacleGrid,
                                                                                                         m, n - 1, mem)
        return mem[m - 1][n - 1]
