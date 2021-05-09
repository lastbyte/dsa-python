'''
Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100

link -> https://leetcode.com/problems/spiral-matrix/
'''
class Solution:
    def spiral_order(self,matrix):
        spiral = []
        return self.spiral_matrix(matrix, 0, len(matrix),0, len(matrix[0]), spiral)

    def spiral_matrix(self,matrix, i_min, i_max, j_min, j_max, spiral):
        i = i_min
        j = j_min

        if (i_max-i_min == 1):
            while j < j_max:
                spiral.append(matrix[i][j])
                j += 1
            return spiral

        if (j_max - j_min == 1):
            while i < i_max:
                spiral.append(matrix[i][j])
                i += 1
            return spiral

        if i_min < i_max and j_min < j_max:
            while j < j_max:
                spiral.append(matrix[i][j])
                j += 1
            j -= 1
            i += 1
            while i < i_max:
                spiral.append(matrix[i][j])
                i += 1
            i -= 1
            j -= 1
            while j >= j_min:
                spiral.append(matrix[i][j])
                j -= 1
            j += 1
            i -= 1
            while i > i_min:
                spiral.append(matrix[i][j])
                i -= 1
            self.spiral_matrix(matrix, i_min + 1, i_max - 1, j_min + 1, j_max - 1, spiral)
        return spiral
