# -*- coding:utf-8 -*-
"""
给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
如果反转后整数超过 32 位的有符号整数的范围 [−2 ** 31,  2 ** 31 − 1] ，就返回 0。
假设环境不允许存储 64 位整数（有符号或无符号）。

示例 1：
输入：x = 123
输出：321

示例 2：
输入：x = -123
输出：-321

示例 3：
输入：x = 120
输出：21

示例 4：
输入：x = 0
输出：0
"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if -10 < x < 10:
            return x
        str_x = str(x)
        if str_x[0] == '-':
            new_str_x = str_x[:0:-1]
            ret = -int(new_str_x)
        else:
            new_str_x = str_x[::-1]
            ret = int(new_str_x)
        return ret if -2147483648 <= ret < 2147483648 else 0


if __name__ == '__main__':
    # 2147483648
    x1 = 123
    x2 = -123
    x3 = 120
    x4 = 0
    s = Solution()
    ret1 = s.reverse(x1)
    ret2 = s.reverse(x2)
    ret3 = s.reverse(x3)
    ret4 = s.reverse(x4)
    print(ret1)
    print(ret2)
    print(ret3)
    print(ret4)
