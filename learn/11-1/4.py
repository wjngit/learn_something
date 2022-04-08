# 剑指 Offer 14- I. 剪绳子
#
# 给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），
# 每段绳子的长度记为 k[0],k[1]...k[m-1] 。请问 k[0]*k[1]*...*k[m-1] 可能的最大乘积是多少？
# 例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。
#
# 示例 1：
# 输入: 2
# 输出: 1
# 解释: 2 = 1 + 1, 1 × 1 = 1
#
# 示例 2:
# 输入: 10
# 输出: 36
# 解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36
#
# 提示：2 <= n <= 58


class Solution:
    def cuttingRope(self, n: int) -> int:
        # if n == 1:
        #     return 1
        # if n == 2:  # 最少要2段
        #     return 1
        # if n == 3:  # 最少要切1刀
        #     return 2
        # # 以下算法在n>=4时才有效
        # # 每一个长度对应的最大乘积，dp[i]表示：长度为i的绳子进行切割后的最大乘积
        # dp = [0] * (n + 1)
        # dp[0] = 1  # 没切，1*长度才能有意义
        # for i in range(1, n + 1):
        #     # 每个长度都可以切1~i这么多段
        #     for j in range(1, i + 1):
        #         # 求出这么多段的最大乘积
        #         # i-1,i-2……i-i
        #         if dp[i] < dp[i - j] * j:
        #             dp[i] = dp[i - j] * j
        # return dp[n]

        pass


if __name__ == '__main__':
    n1 = 2
    n2 = 10

    s = Solution()
    r1 = s.cuttingRope(n1)
    r2 = s.cuttingRope(n2)
    print(r1)
    print(r2)
