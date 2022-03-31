# 面试题 16.19. 水域大小
#
# 你有一个用于表示一片土地的整数矩阵land，该矩阵中每个点的值代表对应地点的海拔高度。
# 若值为0则表示水域。由垂直、水平或对角连接的水域为池塘。池塘的大小是指相连接的水域的个数。
# 编写一个方法来计算矩阵中所有池塘的大小，返回值需要从小到大排序。
#
# 示例：
# 输入：
# [
#   [0,2,1,0],
#   [0,1,0,1],
#   [1,1,0,1],
#   [0,1,0,1]
# ]
# 输出： [1,2,4]
# 提示：
# 0 < len(land) <= 1000
# 0 < len(land[i]) <= 1000


from typing import List


class Solution:
    def pondSizes(self, land: List[List[int]]) -> List[int]:
        #     self.n = len(land)
        #     self.m = len(land[0])
        #     result = []
        #     for i in range(self.n):
        #         for j in range(self.m):
        #             if land[i][j] == 0:
        #                 self.count = 0
        #                 self.dfs(land, i, j)
        #                 result.append(self.count)
        #     result.sort()
        #     return result
        #
        # def __init__(self):
        #     self.count = 0
        #     self.n = 0
        #     self.m = 0
        #
        # def dfs(self, land, i, j):
        #     self.count += 1
        #     land[i][j] = 1
        #     dirs = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [1, 1], [-1, 1], [1, -1]]
        #     for d in range(8):
        #         newi = i + dirs[d][0]
        #         newj = j + dirs[d][1]
        #         if newi >= 0 and newi < self.n and newj >= 0 and newj < self.m and land[newi][newj] == 0:
        #             self.dfs(land, newi, newj)

        pass


if __name__ == '__main__':
    land = [
        [0, 2, 1, 0],
        [0, 1, 0, 1],
        [1, 1, 0, 1],
        [0, 1, 0, 1]
    ]

    s = Solution()
    r = s.pondSizes(land)
    print(r)
