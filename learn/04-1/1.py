# 剑指 Offer 10- I. 斐波那契数列
#
# 写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项（即 F(N)）。斐波那契数列的定义如下：
#     F(0) = 0,   F(1) = 1
#     F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
# 斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。
# 答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。
#
# 示例 1：
# 输入：n = 2
# 输出：1
#
# 示例 2：
# 输入：n = 5
# 输出：5
#
# 提示：0 <= n <= 100


class Solution:
    memo = {}
    mod = 1000000007

    def fib(self, n: int) -> int:
        return self.fib_r(n)

    def fib_r(self, n):
        if n < 2:
            return n
        num = self.memo.get(n)
        if num:
            return num
        data = (self.fib_r(n - 1) + self.fib_r(n - 2)) % self.mod
        self.memo[n] = data
        return data


if __name__ == '__main__':
    n1 = 2
    n2 = 5
    n3 = 10

    s = Solution()
    r1 = s.fib(n1)
    r2 = s.fib(n2)
    r3 = s.fib(n3)
    print(r1)
    print(r2)
    print(r3)
