# 322. 零钱兑换
#
# 给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。
# 计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。
# 你可以认为每种硬币的数量是无限的。
#
# 示例 1：
# 输入：coins = [1, 2, 5], amount = 11
# 输出：3
# 解释：11 = 5 + 5 + 1
#
# 示例 2：
# 输入：coins = [2], amount = 3
# 输出：-1
#
# 示例 3：
# 输入：coins = [1], amount = 0
# 输出：0
#
# 提示：
# 1 <= coins.length <= 12
# 1 <= coins[i] <= 2^31 - 1
# 0 <= amount <= 10^4


from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # k = len(coins)
        # dp = [float("inf")] * (amount + 1)
        # dp[0] = 0
        # for i in range(1, amount + 1):
        #     for j in range(k):
        #         if i - coins[j] >= 0 and dp[i - coins[j]] != float("inf") and dp[i - coins[j]] + 1 < dp[i]:
        #             dp[i] = dp[i - coins[j]] + 1
        # if dp[amount] == float("inf"):
        #     return -1
        # return dp[amount]

        pass


if __name__ == '__main__':
    coins1 = [1, 2, 5]
    amount1 = 11
    coins2 = [2]
    amount2 = 3
    coins3 = [1]
    amount3 = 0
    coins4 = [389, 46, 222, 352, 4, 250]
    amount4 = 5343

    s = Solution()
    r1 = s.coinChange(coins1, amount1)
    r2 = s.coinChange(coins2, amount2)
    r3 = s.coinChange(coins3, amount3)
    r4 = s.coinChange(coins4, amount4)
    print(r1)
    print(r2)
    print(r3)
    print(r4)
