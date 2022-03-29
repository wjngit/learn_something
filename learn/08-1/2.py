# 37. 解数独
#
# 编写一个程序，通过填充空格来解决数独问题。
# 数独的解法需 遵循如下规则：
#     数字 1-9 在每一行只能出现一次。
#     数字 1-9 在每一列只能出现一次。
#     数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图）
#     数独部分空格内已填入了数字，空白格用 '.' 表示。
#
# 示例 1：
# 输入：
# board = [
#     ["5","3",".",".","7",".",".",".","."],
#     ["6",".",".","1","9","5",".",".","."],
#     [".","9","8",".",".",".",".","6","."],
#     ["8",".",".",".","6",".",".",".","3"],
#     ["4",".",".","8",".","3",".",".","1"],
#     ["7",".",".",".","2",".",".",".","6"],
#     [".","6",".",".",".",".","2","8","."],
#     [".",".",".","4","1","9",".",".","5"],
#     [".",".",".",".","8",".",".","7","9"]
# ]
# 输出：
# [
#     ["5","3","4","6","7","8","9","1","2"],
#     ["6","7","2","1","9","5","3","4","8"],
#     ["1","9","8","3","4","2","5","6","7"],
#     ["8","5","9","7","6","1","4","2","3"],
#     ["4","2","6","8","5","3","7","9","1"],
#     ["7","1","3","9","2","4","8","5","6"],
#     ["9","6","1","5","3","7","2","8","4"],
#     ["2","8","7","4","1","9","6","3","5"],
#     ["3","4","5","2","8","6","1","7","9"]
# ]
# 解释：输入的数独如上图所示，唯一有效的解决方案如下所示：
#
# 提示：
#     board.length == 9
#     board[i].length == 9
#     board[i][j] 是一位数字或者 '.'
#     题目数据 保证 输入数独仅有一个解


from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    data = int(board[i][j])
                    self.rows[i][data] = True
                    self.cols[j][data] = True
                    self.blocks[i // 3][j // 3][data] = True
        self.backtrack(board, 0, 0)

    def __init__(self):
        self.solved = False
        self.rows = [[None] * 10 for _ in range(9)]
        self.cols = [[None] * 10 for _ in range(9)]
        self.blocks = [[[None] * 10 for _ in range(3)] for _ in range(3)]

    def backtrack(self, board, row, col):
        if row == 9:
            self.solved = True
            return
        if board[row][col] != ".":
            next_row = row
            next_col = col + 1
            if col == 8:
                next_row = row + 1
                next_col = 0
            self.backtrack(board, next_row, next_col)
            if self.solved:
                return
        else:
            for num in range(1, 10):
                if not self.rows[row][num] and not self.cols[col][num] and not self.blocks[row // 3][col // 3][num]:
                    board[row][col] = str(num)
                    self.rows[row][num] = True
                    self.cols[col][num] = True
                    self.blocks[row // 3][col // 3][num] = True
                    next_row = row
                    next_col = col + 1
                    if col == 8:
                        next_row = row + 1
                        next_col = 0
                    self.backtrack(board, next_row, next_col)
                    if self.solved:
                        return
                    board[row][col] = "."
                    self.rows[row][num] = False
                    self.cols[col][num] = False
                    self.blocks[row // 3][col // 3][num] = False


if __name__ == '__main__':
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    s = Solution()
    s.solveSudoku(board)
    print(board)
