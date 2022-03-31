# 200. 岛屿数量
#
# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
# 岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
# 此外，你可以假设该网格的四条边均被水包围。
#
# 示例 1：
# 输入：grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# 输出：1
#
# 示例 2：
# 输入：grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# 输出：3
#
# 提示：
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] 的值为 '0' 或 '1'


from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #     self.h = len(grid)
        #     self.w = len(grid[0])
        #     self.visited = [[False] * self.w for i in range(self.h)]
        #     for i in range(self.h):
        #         for j in range(self.w):
        #             if grid[i][j] == "1" and self.visited[i][j] != True:
        #                 self.result += 1
        #                 self.dfs(grid, i, j)
        #     return self.result
        #
        # def __init__(self):
        #     self.visited = None
        #     self.h = 0
        #     self.w = 0
        #     self.result = 0
        #
        # def dfs(self, grid, i, j):
        #     directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        #     self.visited[i][j] = True
        #     for k in range(4):
        #         newi = directions[k][0] + i
        #         newj = directions[k][1] + j
        #         if newi >= 0 and newi < self.h and newj >= 0 and newj < self.w and \
        #                 self.visited[newi][newj] != True and grid[newi][newj] == "1":
        #             self.dfs(grid, newi, newj)

        pass


if __name__ == '__main__':
    grid1 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    grid2 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]

    s1 = Solution()
    s2 = Solution()
    r1 = s1.numIslands(grid1)
    r2 = s2.numIslands(grid2)
    print(r1)
    print(r2)
