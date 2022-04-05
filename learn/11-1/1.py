# 70. 爬楼梯
#
# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
#
# 示例 1：
# 输入：n = 2
# 输出：2
# 解释：有两种方法可以爬到楼顶。
# 1. 1 阶 + 1 阶
# 2. 2 阶
#
# 示例 2：
# 输入：n = 3
# 输出：3
# 解释：有三种方法可以爬到楼顶。
# 1. 1 阶 + 1 阶 + 1 阶
# 2. 1 阶 + 2 阶
# 3. 2 阶 + 1 阶
#
# 提示：1 <= n <= 45


class Solution:
    def climbStairs(self, n: int) -> int:
        # dp = [0] * (n + 1)
        # dp[0] = 1
        # for i in range(1, n + 1):
        #     if i - 1 >= 0:
        #         dp[i] += dp[i - 1]
        #     if i - 2 >= 0:
        #         dp[i] += dp[i - 2]
        # return dp[n]

        pass

        # if n <= 2:
        #     return n
        # dp = [0] * (n + 1)
        # dp[1] = 1
        # dp[2] = 2
        # for i in range(3, n + 1):
        #     dp[i] = dp[i - 1] + dp[i - 2]
        # return dp[n]

        pass


if __name__ == '__main__':
    n1 = 1
    n2 = 2
    n3 = 10

    s = Solution()
    r1 = s.climbStairs(n1)
    r2 = s.climbStairs(n2)
    r3 = s.climbStairs(n3)
    print(r1)
    print(r2)
    print(r3)
