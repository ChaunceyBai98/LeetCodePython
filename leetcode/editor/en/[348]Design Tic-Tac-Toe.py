# Assume the following rules are for the tic-tac-toe game on an n x n board 
# between two players: 
# 
#  
#  A move is guaranteed to be valid and is placed on an empty block. 
#  Once a winning condition is reached, no more moves are allowed. 
#  A player who succeeds in placing n of their marks in a horizontal, vertical, 
# or diagonal row wins the game. 
#  
# 
#  Implement the TicTacToe class: 
# 
#  
#  TicTacToe(int n) Initializes the object the size of the board n. 
#  int move(int row, int col, int player) Indicates that the player with id 
# player plays at the cell (row, col) of the board. The move is guaranteed to be a 
# valid move. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input
# ["TicTacToe", "move", "move", "move", "move", "move", "move", "move"]
# [[3], [0, 0, 1], [0, 2, 2], [2, 2, 1], [1, 1, 2], [2, 0, 1], [1, 0, 2], [2, 1,
#  1]]
# Output
# [null, 0, 0, 0, 0, 0, 0, 1]
# 
# Explanation
# TicTacToe ticTacToe = new TicTacToe(3);
# Assume that player 1 is "X" and player 2 is "O" in the board.
# ticTacToe.move(0, 0, 1); // return 0 (no one wins)
# |X| | |
# | | | |    // Player 1 makes a move at (0, 0).
# | | | |
# 
# ticTacToe.move(0, 2, 2); // return 0 (no one wins)
# |X| |O|
# | | | |    // Player 2 makes a move at (0, 2).
# | | | |
# 
# ticTacToe.move(2, 2, 1); // return 0 (no one wins)
# |X| |O|
# | | | |    // Player 1 makes a move at (2, 2).
# | | |X|
# 
# ticTacToe.move(1, 1, 2); // return 0 (no one wins)
# |X| |O|
# | |O| |    // Player 2 makes a move at (1, 1).
# | | |X|
# 
# ticTacToe.move(2, 0, 1); // return 0 (no one wins)
# |X| |O|
# | |O| |    // Player 1 makes a move at (2, 0).
# |X| |X|
# 
# ticTacToe.move(1, 0, 2); // return 0 (no one wins)
# |X| |O|
# |O|O| |    // Player 2 makes a move at (1, 0).
# |X| |X|
# 
# ticTacToe.move(2, 1, 1); // return 1 (player 1 wins)
# |X| |O|
# |O|O| |    // Player 1 makes a move at (2, 1).
# |X|X|X|
#  
# 
#  
#  Constraints: 
# 
#  
#  2 <= n <= 100 
#  player is 1 or 2. 
#  0 <= row, col < n 
#  (row, col) are unique for each different call to move. 
#  At most n² calls will be made to move. 
#  
# 
#  
#  Follow-up: Could you do better than O(n²) per move() operation? 
#  Related Topics Array Hash Table Design Matrix 👍 1688 👎 98

from typing import List, Optional
from dataStructure.ListNode import ListNode


# leetcode submit region begin(Prohibit modification and deletion)
class TicTacToe:
    # O(n)
    # def __init__(self, n: int):
    #     self.board = [[''] * n for _ in range(n)]
    #
    # def move(self, row: int, col: int, player: int) -> int:
    #     n = len(self.board)
    #     if player == 1:
    #         mark = 'x'
    #     else:
    #         mark = 'o'
    #     self.board[row][col] = mark
    #     sum_row = sum([self.board[row][c] == mark for c in range(n)])
    #     sum_col = sum([self.board[r][col] == mark for r in range(n)])
    #     sum_left_d = sum([self.board[i][i] == mark for i in range(n)])
    #     sum_right_d = sum([self.board[i][n-1-i] == mark for i in range(n)])
    #     if sum_row == n or sum_col == n or sum_left_d == n or sum_right_d == n:
    #         return player
    #     else:
    #         return 0

    # O(1)
    def __init__(self, n: int):
        self.rows = [0] * n
        self.cols = [0] * n
        self.diag1 = 0
        self.diag2 = 0
        self.size = n

    def move(self, row: int, col: int, player: int) -> int:
        if player == 1:
            temp = 1
        else:
            temp = -1

        self.rows[row] += temp
        self.cols[col] += temp

        if row == col:
            self.diag1 += temp
        if row + col == self.size - 1:
            self.diag2 += temp

        if (self.rows[row] == self.size or self.cols[col] == self.size
                or self.diag1 == self.size or self.diag2 == self.size):
            return player
        if (self.rows[row] == -self.size or self.cols[col] == -self.size
                or self.diag1 == -self.size or self.diag2 == -self.size):
            return player

        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    a = TicTacToe(10)
    a.move()

