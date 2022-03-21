# 剑指 Offer 10- II. 青蛙跳台阶问题
#
# 一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。
# 答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。
#
# 示例 1：
# 输入：n = 2
# 输出：2
#
# 示例 2：
# 输入：n = 7
# 输出：21
#
# 示例 3：
# 输入：n = 0
# 输出：1
#
# 提示：0 <= n <= 100


class Solution:
    mod = 1000000007
    memo = {}

    def numWays(self, n: int) -> int:
        #     return self.numWays_r(n)
        #
        # def numWays_r(self, n):
        #     if n == 0:
        #         return 1
        #     if n == 1:
        #         return 1
        #     num = self.memo.get(n)
        #     if num:
        #         return num
        #     data = (self.numWays_r(n - 1) + self.numWays_r(n - 2)) % self.mod
        #     self.memo[n] = data
        #     return data

        pass


if __name__ == '__main__':
    n1 = 2
    n2 = 7
    n3 = 0

    s = Solution()
    r1 = s.numWays(n1)
    r2 = s.numWays(n2)
    r3 = s.numWays(n3)
    print(r1)
    print(r2)
    print(r3)
