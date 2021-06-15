from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(len(triangle)):
            for j in range(i+1):
                if i == 0:
                    continue
                else:
                    k = float('inf') if j==0 else triangle[i-1][j-1]
                    l = float('inf') if j == i else triangle[i-1][j]
                    triangle[i][j] = triangle[i][j] + min(triangle[i-1][j-1] , triangle)
        minimum = float('inf')
        for i in triangle[len(triangle)]:
            if minimum > i:
                minimum = i
        return minimum