# 剑指 Offer 46. 把数字翻译成字符串
#
# 给定一个数字，我们按照如下规则把它翻译为字符串：
# 0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。
# 一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。
#
# 示例 1:
# 输入: 12258
# 输出: 5
# 解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"
#
# 提示：0 <= num < 2^31


class Solution:
    def translateNum(self, num: int) -> int:
        if num <= 9:
            return 1
        digitlist = []
        while num != 0:
            digitlist.append(num % 10)
            num = num // 10
        n = len(digitlist)
        digits = []
        for i in range(n):
            digits.append(digitlist[n - i - 1])
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            dp[i] = dp[i - 1]
            if i - 2 >= 0 and self.isValid(digits[i - 2], digits[i - 1]):
                dp[i] += dp[i - 2]
        return dp[n]

    def isValid(self, a, b):
        if a == 1:
            return True
        if a == 2 and 0 <= b <= 5:
            return True
        return False


if __name__ == '__main__':
    num = 12258

    s = Solution()
    r = s.translateNum(num)
    print(r)
