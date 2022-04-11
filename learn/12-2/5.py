# 面试题 05.01. 插入
#
# 给定两个整型数字 N 与 M，以及表示比特位置的 i 与 j（i <= j，且从 0 位开始计算）。
# 编写一种方法，使 M 对应的二进制数字插入 N 对应的二进制数字的第 i ~ j 位区域，不足之处用 0 补齐。具体插入过程如图所示。
# 题目保证从 i 位到 j 位足以容纳 M， 例如： M = 10011，则 i～j 区域至少可容纳 5 位。
#
# 示例1:
#  输入：N = 1024(10000000000), M = 19(10011), i = 2, j = 6
#  输出：N = 1100(10001001100)
#
# 示例2:
#  输入： N = 0, M = 31(11111), i = 0, j = 4
#  输出：N = 31(11111)


class Solution:
    def insertBits(self, N: int, M: int, i: int, j: int) -> int:
        nbits = [0] * 32
        mbits = [0] * 32
        nbitsNum = 0
        mbitsNum = 0
        mask = 1
        for k in range(32):
            if (N & mask) != 0:
                nbits[k] = 1
            mask <<= 1
        mask = 1
        for k in range(32):
            if (M & mask) != 0:
                mbits[k] = 1
            mask <<= 1
        for k in range(i, j + 1):
            nbits[k] = mbits[k - i]
        mask = 1
        ret = 0
        for k in range(32):
            ret += (nbits[k] * mask)
            mask <<= 1
        return ret


if __name__ == '__main__':
    n1, m1, i1, j1 = 1024, 19, 2, 6
    n2, m2, i2, j2 = 0, 31, 0, 4

    s = Solution()
    r1 = s.insertBits(n1, m1, i1, j1)
    r2 = s.insertBits(n2, m2, i2, j2)
    print(r1)
    print(r2)
