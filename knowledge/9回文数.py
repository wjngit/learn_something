# -*- coding:utf-8 -*-
"""
给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。
回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。例如，121 是回文，而 123 不是。

示例 1：
输入：x = 121
输出：true

示例 2：
输入：x = -121
输出：false
解释：从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。

示例 3：
输入：x = 10
输出：false
解释：从右向左读, 为 01 。因此它不是一个回文数。

示例 4：
输入：x = -101
输出：false
"""


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x % 10 == 0:
            return False
        return True if str(x)[::-1] == str(x) else False
        # ************************************
        # tmp1 = str(x)
        # tmp2 = tmp1[::-1]
        # if tmp2[-1] == '-':
        #     return False
        # if int(tmp2) == x:
        #     return True
        # else:
        #     return False


if __name__ == '__main__':
    x1 = 121
    x2 = -121
    x3 = 10
    x4 = -101
    s = Solution()
    ret1 = s.isPalindrome(x1)
    ret2 = s.isPalindrome(x2)
    ret3 = s.isPalindrome(x3)
    ret4 = s.isPalindrome(x4)
    print(ret1)
    print(ret2)
    print(ret3)
    print(ret4)
