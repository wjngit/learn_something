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
        #     m, n = len(land), len(land[0])
        #     result = []
        #     for i in range(m):
        #         for j in range(n):
        #             if land[i][j] == 0:
        #                 self.count = 0
        #                 self.dfs(land, i, j, m, n)
        #                 result.append(self.count)
        #     result.sort()
        #     return result
        #
        # def __init__(self):
        #     self.count = 0
        #
        # def dfs(self, land, i, j, m, n):
        #     self.count += 1
        #     land[i][j] = 1
        #     dirs = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [1, 1], [-1, 1], [1, -1]]
        #     for data in dirs:
        #         new_i = i + data[0]
        #         new_j = j + data[1]
        #         if 0 <= new_i < m and 0 <= new_j < n and land[new_i][new_j] == 0:
        #             self.dfs(land, new_i, new_j, m, n)

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
