# 120. 三角形最小路径和
#
# 给定一个三角形 triangle ，找出自顶向下的最小路径和。
# 每一步只能移动到下一行中相邻的结点上。
# 相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。
# 也就是说，如果正位于当前行的下标 i ，那么下一步可以移动到下一行的下标 i 或 i + 1 。
#
# 示例 1：
# 输入：triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# 输出：11
# 解释：如下面简图所示：
#    2
#   3 4
#  6 5 7
# 4 1 8 3
# 自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
#
# 示例 2：
# 输入：triangle = [[-10]]
# 输出：-10
#
# 提示：
# 1 <= triangle.length <= 200
# triangle[0].length == 1
# triangle[i].length == triangle[i - 1].length + 1
# -104 <= triangle[i][j] <= 104
#
# 进阶：你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题吗？


from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # n = len(triangle)
        # dp = [[float("inf")] * n for _ in range(n)]
        # dp[0][0] = triangle[0][0]
        # for i in range(1, n):
        #     dp[i][0] = dp[i - 1][0] + triangle[i][0]
        #     for j in range(1, i):
        #         dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1]) + triangle[i][j]
        #     dp[i][i] = dp[i - 1][i - 1] + triangle[i][i]
        # res = float("inf")
        # for j in range(n):
        #     if dp[n - 1][j] < res:
        #         res = dp[n - 1][j]
        # return res

        pass


if __name__ == '__main__':
    triangle1 = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    triangle2 = [[-10]]

    s = Solution()
    r1 = s.minimumTotal(triangle1)
    r2 = s.minimumTotal(triangle2)
    print(r1)
    print(r2)
