# 面试题 08.05. 递归乘法
#
# 递归乘法。 写一个递归函数，不使用 * 运算符， 实现两个正整数的相乘。可以使用加号、减号、位移，但要吝啬一些。
#
# 示例1:
#  输入：A = 1, B = 10
#  输出：10
#
# 示例2:
#  输入：A = 3, B = 4
#  输出：12
#
# 提示:保证乘法范围不会溢出


class Solution:
    def multiply(self, A: int, B: int) -> int:
        # if A == 1:
        #     return B
        # half = self.multiply(A // 2, B)
        # if A % 2 == 1:
        #     return half + half + B
        # return half + half

        pass


if __name__ == '__main__':
    x1 = 2
    n1 = 10
    x2 = 2
    n2 = 3
    x3 = 3
    n3 = -2

    s = Solution()
    r1 = s.multiply(x1, n1)
    r2 = s.multiply(x2, n2)
    r3 = s.multiply(x3, n3)
    print(r1)
    print(r2)
    print(r3)
