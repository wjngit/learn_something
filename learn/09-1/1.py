# 剑指 Offer 13. 机器人的运动范围
#
# 地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，
# 它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。
# 例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。
# 请问该机器人能够到达多少个格子？
#
# 示例 1：
# 输入：m = 2, n = 3, k = 1
# 输出：3
#
# 示例 2：
# 输入：m = 3, n = 1, k = 0
# 输出：1
#
# 提示：
# 1 <= n,m <= 100
# 0 <= k <= 20


class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        #     self.visited = [[False] * n for _ in range(m)]
        #     self.dfs(0, 0, m, n, k)
        #     return self.count
        #
        # def __init__(self):
        #     self.visited = None
        #     self.count = 0
        #
        # def dfs(self, i, j, m, n, k):
        #     self.visited[i][j] = True
        #     self.count += 1
        #     directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        #     for di in directions:
        #         newi = i + di[0]
        #         newj = j + di[1]
        #         if newi >= m or newi < 0 or newj >= n or newj < 0 or self.visited[newi][newj] or \
        #                 self.check(newi, newj, k) == False:
        #             continue
        #         self.dfs(newi, newj, m, n, k)
        #
        # def check(self, i, j, k):
        #     total = 0
        #     while i > 0:
        #         total += i % 10
        #         i //= 10
        #     while j > 0:
        #         total += j % 10
        #         j //= 10
        #     return total <= k

        pass


if __name__ == '__main__':
    m1 = 2
    n1 = 3
    k1 = 1
    m2 = 3
    n2 = 1
    k2 = 0

    s1 = Solution()
    s2 = Solution()
    r1 = s1.movingCount(m1, n1, k1)
    r2 = s2.movingCount(m2, n2, k2)
    print(r1)
    print(r2)
