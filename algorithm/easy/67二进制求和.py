# -*- coding:utf-8 -*-
"""
给你两个二进制字符串，返回它们的和（用二进制表示）。
输入为 非空 字符串且只包含数字 1 和 0。

示例 1:
输入: a = "11", b = "1"
输出: "100"

示例 2:
输入: a = "1010", b = "1011"
输出: "10101"
"""


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        num_a = int(a, 2)
        print(num_a)
        num_b = int(b, 2)
        print(num_b)
        print(bin(num_a + num_b))
        return bin(num_a + num_b)[2:]

        pass


if __name__ == '__main__':
    a1, b1 = '11', '1'
    a2, b2 = '1010', '1011'
    s = Solution()
    ret1 = s.addBinary(a1, b1)
    ret2 = s.addBinary(a2, b2)
    print(ret1)
    print(ret2)
