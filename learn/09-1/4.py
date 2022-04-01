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
        #     m, n = len(grid), len(grid[0])
        #     self.visited = [[False] * n for _ in range(m)]
        #     for i in range(m):
        #         for j in range(n):
        #             if grid[i][j] == "1" and self.visited[i][j] is not True:
        #                 self.result += 1
        #                 self.dfs(grid, i, j, m, n)
        #     return self.result
        #
        # def __init__(self):
        #     self.visited = None
        #     self.result = 0
        #
        # def dfs(self, grid, i, j, m, n):
        #     self.visited[i][j] = True
        #     for data in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        #         new_i = data[0] + i
        #         new_j = data[1] + j
        #         if 0 <= new_i < m and 0 <= new_j < n and self.visited[new_i][new_j] is not True and \
        #                 grid[new_i][new_j] == "1":
        #             self.dfs(grid, new_i, new_j, m, n)

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
