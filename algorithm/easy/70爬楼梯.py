# -*- coding:utf-8 -*-
"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
注意：给定 n 是一个正整数。

示例 1：
输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶

示例 2：
输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶
"""


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # if n <= 2:
        #     return n
        # i, j, k = 1, 2, 3
        # ret_sum = 0
        # while k <= n:
        #     ret_sum = i + j
        #     i = j
        #     j = ret_sum
        #     k += 1
        # return ret_sum

        pass


if __name__ == '__main__':
    n1 = 2
    n2 = 44
    s = Solution()
    ret1 = s.climbStairs(n1)
    ret2 = s.climbStairs(n2)
    print(ret1)
    print(ret2)
    pass
