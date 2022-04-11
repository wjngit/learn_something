# 面试题 05.06. 整数转换
#
# 整数转换。编写一个函数，确定需要改变几个位才能将整数A转成整数B。
#
# 示例1:
#  输入：A = 29 （或者0b11101）, B = 15（或者0b01111）
#  输出：2
#
# 示例2:
#  输入：A = 1，B = 2
#  输出：2
#
# 提示:A，B范围在[-2147483648, 2147483647]之间


class Solution:
    def convertInteger(self, A: int, B: int) -> int:
        C = A ^ B
        count = 0
        for i in range(32):
            if (C & 1) == 1:
                count += 1
            C >>= 1
        return count


if __name__ == '__main__':
    a1 = 29
    b1 = 15
    a2 = 1
    b2 = 2

    s = Solution()
    r1 = s.convertInteger(a1, b1)
    r2 = s.convertInteger(a2, b2)
    print(r1)
    print(r2)
