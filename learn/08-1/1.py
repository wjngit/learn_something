# 面试题 08.12. 八皇后
#
# 设计一种算法，打印 N 皇后在 N × N 棋盘上的各种摆法，其中每个皇后都不同行、不同列，也不在对角线上。
# 这里的“对角线”指的是所有的对角线，不只是平分整个棋盘的那两条对角线。
# 注意：本题相对原题做了扩展
#
# 示例:
# 输入：4
# 输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# 解释: 4 皇后问题存在如下两个不同的解法。
# [
#  [".Q..",  // 解法 1
#   "...Q",
#   "Q...",
#   "..Q."],
#
#  ["..Q.",  // 解法 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]


from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        #     board = [["."] * n for _ in range(n)]
        #     self.backtrack(0, board, n)
        #     return self.result
        #
        # def __init__(self):
        #     self.result = []
        #
        # def backtrack(self, row, board, n):
        #     if row == n:
        #         snapshot = []
        #         for i in range(n):
        #             snapshot.append("".join(board[i]))
        #         self.result.append(snapshot)
        #         return
        #     for col in range(n):
        #         if self.is_ok(board, n, row, col):
        #             board[row][col] = "Q"
        #             self.backtrack(row + 1, board, n)
        #             board[row][col] = "."
        #
        # def is_ok(self, board, n, row, col):
        #     for i in range(n):
        #         if board[i][col] == "Q":
        #             return False
        #     # 右上角
        #     i, j = row - 1, col + 1
        #     while i >= 0 and j < n:
        #         if board[i][j] == "Q":
        #             return False
        #         i -= 1
        #         j += 1
        #     # 左上角
        #     i, j = row - 1, col - 1
        #     while i >= 0 and j >= 0:
        #         if board[i][j] == "Q":
        #             return False
        #         i -= 1
        #         j -= 1
        #     return True

        pass


if __name__ == '__main__':
    n = 4

    s = Solution()
    r = s.solveNQueens(n)
    print(r)
