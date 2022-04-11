# 面试题 05.07. 配对交换
#
# 配对交换。编写程序，交换某个整数的奇数位和偶数位，尽量使用较少的指令（也就是说，位0与位1交换，位2与位3交换，以此类推）。
#
# 示例1:
#  输入：num = 2（或者0b10）
#  输出 1 (或者 0b01)
#
# 示例2:
#  输入：num = 3
#  输出：3
#
# 提示:num的范围在[0, 2^30 - 1]之间，不会发生整数溢出。

class Solution:
    def exchangeBits(self, num: int) -> int:
        ret = 0
        for i in range(0, 30, 2):
            a1 = (num & (1 << i))
            b1 = (num & (1 << (i + 1)))
            if a1 != 0:
                ret |= (1 << (i + 1))
            if b1 != 0:
                ret |= (1 << i)
        return ret


if __name__ == '__main__':
    num1 = 2
    num2 = 3

    s = Solution()
    r1 = s.exchangeBits(num1)
    r2 = s.exchangeBits(num2)
    print(r1)
    print(r2)
