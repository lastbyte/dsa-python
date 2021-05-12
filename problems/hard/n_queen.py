'''
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

 

Example 1:


Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
Example 2:

Input: n = 1
Output: [["Q"]]
 

Constraints:

1 <= n <= 9

link -> https://leetcode.com/problems/n-queens/
'''


class Solution:
    def n_queen(self, n):
        board = [['.'] * n for i in range(n)]
        solutions = []
        cols = {}
        for i in range(n):
            cols[i] = False
        self.place_queen(board, n, 0, cols, solutions)
        return solutions

    def place_queen(self, board, n, queens, cols, solutions):
        if queens == n:
            solution = [''.join(row) for row in board]
            solutions.append(solution)
        if queens < n:
            for j in range(n):
                if not cols[j] and self.is_valid_position(board, queens, j, n):
                    board[queens][j] = 'Q'
                    cols[j] = True
                    self.place_queen(board, n, queens + 1, cols, solutions)
                    board[queens][j] = '.'
                    cols[j] = False

    def is_valid_position(self, board, i, j, n):
        for k in range(n):
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