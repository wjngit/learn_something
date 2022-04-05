# 714. 买卖股票的最佳时机含手续费
#
# 给定一个整数数组 prices，其中 prices[i]表示第 i 天的股票价格 ；整数 fee 代表了交易股票的手续费用。
# 你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。
# 返回获得利润的最大值。
# 注意：这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。
#
# 示例 1：
# 输入：prices = [1, 3, 2, 8, 4, 9], fee = 2
# 输出：8
# 解释：能够达到的最大利润:
# 在此处买入 prices[0] = 1
# 在此处卖出 prices[3] = 8
# 在此处买入 prices[4] = 4
# 在此处卖出 prices[5] = 9
# 总利润: ((8 - 1) - 2) + ((9 - 4) - 2) = 8
#
# 示例 2：
# 输入：prices = [1,3,7,5,10,3], fee = 3
# 输出：6
#
# 提示：
# 1 <= prices.length <= 5 * 10^4
# 1 <= prices[i] < 5 * 10^4
# 0 <= fee < 5 * 10^4


from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # n = len(prices)
        # # 不持有股票和持有股票可赚到最大利润（存的数据表示利润）
        # dp = [[0, 0] for _ in range(n)]
        # dp[0][0] = -prices[0]  # 持有股票
        # dp[0][1] = 0  # 不持有股票
        # for i in range(1, n):
        #     # 持有：前一天也持有，就是2天不变；前一天不持有，那么今天就要买入
        #     dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i])
        #     # 不持有：前一天持有，今天不持有，那么就是卖出；前一天不持有，就是2天不变
        #     dp[i][1] = max(dp[i - 1][0] + prices[i] - fee, dp[i - 1][1])
        # return max(dp[n - 1][0], dp[n - 1][1])

        pass


if __name__ == '__main__':
    prices1 = [1, 3, 2, 8, 4, 9]
    fee1 = 2
    prices2 = [1, 3, 7, 5, 10, 3]
    fee2 = 3

    s = Solution()
    r1 = s.maxProfit(prices1, fee1)
    r2 = s.maxProfit(prices2, fee2)
    print(r1)
    print(r2)
