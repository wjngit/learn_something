# 面试题 16.04. 井字游戏
#
# 设计一个算法，判断玩家是否赢了井字游戏。
# 输入是一个 N x N 的数组棋盘，由字符" "，"X"和"O"组成，其中字符" "代表一个空位。
#
# 以下是井字游戏的规则：
#     玩家轮流将字符放入空位（" "）中。
#     第一个玩家总是放字符"O"，且第二个玩家总是放字符"X"。
#     "X"和"O"只允许放置在空位中，不允许对已放有字符的位置进行填充。
#     当有N个相同（且非空）的字符填充任何行、列或对角线时，游戏结束，对应该字符的玩家获胜。
#     当所有位置非空时，也算为游戏结束。
#     如果游戏结束，玩家不允许再放置字符。
#     如果游戏存在获胜者，就返回该游戏的获胜者使用的字符（"X"或"O"）；
#     如果游戏以平局结束，则返回 "Draw"；如果仍会有行动（游戏未结束），则返回 "Pending"。
#
# 示例 1：
# 输入： board = ["O X"," XO","X O"]
# 输出： "X"
#
# 示例 2：
# 输入： board = ["OOX","XXO","OXO"]
# 输出： "Draw"
# 解释： 没有玩家获胜且不存在空位
#
# 示例 3：
# 输入： board = ["OOX","XXO","OX "]
# 输出： "Pending"
# 解释： 没有玩家获胜且仍存在空位
#
# 提示：
#     1 <= board.length == board[i].length <= 100
#     输入一定遵循井字棋规则

from typing import List


class Solution:
    def tictactoe(self, board: List[str]) -> str:
        # n = len(board)
        # boards = [[]] * n
        # for i in range(n):
        #     boards[i] = list(board[i])
        #
        # # 检查⾏
        # for i in range(n):
        #     if boards[i][0] == " ":
        #         continue
        #     determined = True
        #     for j in range(1, n):
        #         if boards[i][j] != boards[i][0]:
        #             determined = False
        #             break
        #     if determined:
        #         return boards[i][0]
        #
        # # 检查列
        # for j in range(n):
        #     if boards[0][j] == " ":
        #         continue
        #     determined = True
        #     for i in range(1, n):
        #         if boards[i][j] != boards[0][j]:
        #             determined = False
        #             break
        #     if determined:
        #         return boards[0][j]
        #
        # # 检查对⻆线左上->右下
        # if boards[0][0] != " ":
        #     i = 0
        #     j = 0
        #     determined = True
        #     while i < n and j < n:
        #         if boards[i][j] != boards[0][0]:
        #             determined = False
        #             break
        #         i += 1
        #         j += 1
        #     if determined:
        #         return boards[0][0]
        #
        # # 检查对⻆线左下->右上
        # if boards[n - 1][0] != " ":
        #     i = n - 2
        #     j = 1
        #     determined = True
        #     while i >= 0 and j < n:
        #         if boards[i][j] != boards[n - 1][0]:
        #             determined = False
        #             break
        #         i -= 1
        #         j += 1
        #     if determined:
        #         return boards[n - 1][0]
        #
        # for i in range(n):
        #     for j in range(n):
        #         if boards[i][j] == " ":
        #             return "Pending"
        # return "Draw"

        pass


if __name__ == '__main__':
    board1 = ["O X", " XO", "X O"]
    board2 = ["OOX", "XXO", "OXO"]
    board3 = ["OOX", "XXO", "OX "]

    s = Solution()
    r1 = s.tictactoe(board1)
    r2 = s.tictactoe(board2)
    r3 = s.tictactoe(board3)
    print(r1)
    print(r2)
    print(r3)
