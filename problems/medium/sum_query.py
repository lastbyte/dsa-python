'''
Given a 2D matrix matrix, handle multiple queries of the following type:

Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
Implement the NumMatrix class:

NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
 

Example 1:


Input
["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
[[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
Output
[null, 8, 11, 12]

Explanation
NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
numMatrix.sumRegion(2, 1, 4, 3); // return 8 (i.e sum of the red rectangle)
numMatrix.sumRegion(1, 1, 2, 2); // return 11 (i.e sum of the green rectangle)
numMatrix.sumRegion(1, 2, 2, 4); // return 12 (i.e sum of the blue rectangle)

link -> https://leetcode.com/problems/range-sum-query-2d-immutable/
'''
class NumMatrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.mem = [[0] * len(matrix[0]) for i in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if j == 0:
                    self.mem[i][j] = matrix[i][j]
                else:
                    self.mem[i][j] = self.mem[i][j - 1] + self.matrix[i][j]
        print(self.mem)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ret_sum = 0
        for i in range(row1, row2 + 1):
            if col1 == 0:
                ret_sum += self.mem[i][col2]
            else:
                ret_sum += (self.mem[i][col2] - self.mem[i][col1 - 1])
        return ret_sum

if __name__ == "__main__":
    solution = NumMatrix([[-4,-5]])
    result = solution.sumRegion(0,1,0,1)
    print(result)