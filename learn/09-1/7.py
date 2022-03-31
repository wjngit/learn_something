# 79. 单词搜索
#
# 给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。
# 如果 word 存在于网格中，返回 true ；否则，返回 false 。
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。
# 同一个单元格内的字母不允许被重复使用。
#
# 示例 1：
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# 输出：true
#
# 示例 2：
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# 输出：true
#
# 示例 3：
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# 输出：false
#
# 提示：
# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board 和 word 仅由大小写英文字母组成
#
# 进阶：你可以使用搜索剪枝的技术来优化解决方案，使其在 board 更大的情况下可以更快解决问题？


from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #     self.exist_ = False
        #     self.h = len(board)
        #     self.w = len(board[0])
        #     for i in range(self.h):
        #         for j in range(self.w):
        #             visited = [[False] * self.w for i in range(self.h)]
        #             self.dfs(board, word, i, j, 0, visited)
        #             if self.exist_:
        #                 return self.exist_
        #     return self.exist_
        #
        # def __init__(self):
        #     self.h = 0
        #     self.w = 0
        #
        # def dfs(self, board, word, i, j, k, visited):
        #     if self.exist_ == True:
        #         return
        #     if word[k] != board[i][j]:
        #         return
        #     visited[i][j] = True
        #     if k == (len(word) - 1):
        #         self.exist_ = True
        #         return
        #     directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        #     for d in range(4):
        #         nexti = i + directions[d][0]
        #         nextj = j + directions[d][1]
        #         if nexti >= 0 and nexti < self.h and nextj >= 0 and nextj < self.w and not visited[nexti][nextj]:
        #             self.dfs(board, word, nexti, nextj, k + 1, visited)
        #     visited[i][j] = False

        pass


if __name__ == '__main__':
    board1 = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word1 = "ABCCED"
    board2 = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word2 = "SEE"
    board3 = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word3 = "ABCB"

    s1 = Solution()
    s2 = Solution()
    s3 = Solution()
    r1 = s1.exist(board1, word1)
    r2 = s2.exist(board2, word2)
    r3 = s3.exist(board3, word3)
    print(r1)
    print(r2)
    print(r3)
