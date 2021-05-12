'''
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

 

Example 1:


Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
Example 2:

Input: n = 1
Output: 1

link -> https://leetcode.com/problems/n-queens-ii/
'''


class Solution:
    def n_queen(self, n):
        board = [['.'] * n for i in range(n)]
        solutions = [0]
        self.place_queen(board, n, 0, solutions)
        return solutions[0]

    def place_queen(self, board, n, queens, solutions):
        if queens == n:
            solutions[0]+=1
        if queens < n:
            for j in range(n):
                if self.is_valid_position(board, queens, j, n):
                    board[queens][j] = 'Q'
                    self.place_queen(board, n, queens + 1, solutions)
                    board[queens][j] = '.'

    def is_valid_position(self, board, i, j, n):
        for k in range(n):
            if board[i][k] == 'Q' or board[k][j] == 'Q':
                return False
            if i - k >= 0 and j - k >= 0 and board[i - k][j - k] == 'Q':
                return False
            if i - k >= 0 and j + k < n and board[i - k][j + k] == 'Q':
                return False
            if i + k < n and j - k >= 0 and board[i + k][j - k] == 'Q':
                return False
            if i + k < n and j + k < n and board[i + k][j + k] == 'Q':
                return False
        return True


if __name__ == "__main__":
    solution = Solution()
    result = solution.n_queen(8)
    print(result)