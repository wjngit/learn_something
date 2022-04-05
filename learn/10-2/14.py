# 309. 最佳买卖股票时机含冷冻期
#
# 给定一个整数数组prices，其中第  prices[i] 表示第 i 天的股票价格 。
# 设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
# 卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
#
# 示例 1:
# 输入: prices = [1,2,3,0,2]
# 输出: 3
# 解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]
#
# 示例 2:
# 输入: prices = [1]
# 输出: 0
#
# 提示：
# 1 <= prices.length <= 5000
# 0 <= prices[i] <= 1000


from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # if len(prices) == 0:
        #     return 0
        # n = len(prices)
        # dp = [[0, 0, 0, 0] for _ in range(n)]
        # dp[0][0] = -prices[0]  # 当天持有股票的利润
        # dp[0][1] = 0  # 当天不持有股票，今天刚卖掉
        # dp[0][2] = 0  # 当天不持有股票，昨天刚卖掉，处于冷冻期
        # dp[0][3] = 0  # 当天不持有股票，非冷冻期，昨天也不持有
        # for i in range(1, n):
        #     # 当天持有：前一天也持有，不变，直接拿过来；前一天冷冻期，今天可以买；前一天非冷冻期，今天可以买
        #     dp[i][0] = max(dp[i - 1][0], dp[i - 1][2] - prices[i], dp[i - 1][3] - prices[i])
        #     # 当天卖掉：前一天持有，今天卖掉，可以进账
        #     dp[i][1] = dp[i - 1][0] + prices[i]
        #     # 今天冷冻期：昨天只能是状态1（刚卖掉）
        #     dp[i][2] = dp[i - 1][1]
        #     # 今天非冷冻期：昨天是状态2或状态3
        #     dp[i][3] = max(dp[i - 1][2], dp[i - 1][3])
        # return max(dp[n - 1][0], dp[n - 1][1], dp[n - 1][2], dp[n - 1][3])

        pass


if __name__ == '__main__':
    prices1 = [1, 2, 3, 0, 2]
    prices2 = [1]

    s = Solution()
    r1 = s.maxProfit(prices1)
    r2 = s.maxProfit(prices2)
    print(r1)
    print(r2)
