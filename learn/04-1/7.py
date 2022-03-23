# 剑指 Offer 16. 数值的整数次方
#
# 实现 pow(x, n) ，即计算 x 的 n 次幂函数（即，x ** n）。不得使用库函数，同时不需要考虑大数问题。
#
# 示例 1：
# 输入：x = 2.00000, n = 10
# 输出：1024.00000
#
# 示例 2：
# 输入：x = 2.10000, n = 3
# 输出：9.26100
#
# 示例 3：
# 输入：x = 2.00000, n = -2
# 输出：0.25000
# 解释：2^-2 = 1/2^2 = 1/4 = 0.25

class Solution:
    def myPow(self, x: float, n: int) -> float:
        #     if n >= 0:
        #         return self.pow_r(x, n)
        #     else:
        #         return 1 / (self.pow_r(x, -1 * (n + 1)) * x)
        #
        # def pow_r(self, x, n):
        #     if n == 0:
        #         return 1
        #     half = self.pow_r(x, n // 2)
        #     if n % 2 == 1:
        #         return half * half * x
        #     return half * half

        pass


if __name__ == '__main__':
    x1 = 2.00000
    n1 = 10
    x2 = 2.10000
    n2 = 3
    x3 = 2.00000
    n3 = -2

    s = Solution()
    r1 = s.myPow(x1, n1)
    r2 = s.myPow(x2, n2)
    r3 = s.myPow(x3, n3)
    print(r1)
    print(r2)
    print(r3)
