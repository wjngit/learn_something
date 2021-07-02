# -*- coding:utf-8 -*-
"""
给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1：
输入：digits = [1,2,3]
输出：[1,2,4]
解释：输入数组表示数字 123。

示例 2：
输入：digits = [4,3,2,1]
输出：[4,3,2,2]
解释：输入数组表示数字 4321。

示例 3：
输入：digits = [0]
输出：[1]
"""


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        tmp_str = ''
        for i in digits:
            tmp_str += str(i)
        tmp_int = int(tmp_str)
        new_str = str(tmp_int + 1) if tmp_int > 0 else '1'
        return [int(i) for i in new_str]

        pass


if __name__ == '__main__':
    digits1 = [1, 2, 3]
    digits2 = [4, 3, 2, 1]
    digits3 = [0]
    s = Solution()
    ret1 = s.plusOne(digits1)
    ret2 = s.plusOne(digits2)
    ret3 = s.plusOne(digits3)
    print(ret1)
    print(ret2)
    print(ret3)
