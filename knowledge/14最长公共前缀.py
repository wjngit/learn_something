# -*- coding:utf-8 -*-
"""
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。

示例 1：
输入：strs = ["flower","flow","flight"]
输出："fl"

示例 2：
输入：strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。
"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # if not strs:
        #     return ''
        # first = strs[0]
        # length, count = len(first), len(strs)
        # for i in range(length):
        #     target = first[i]
        #     judge_list = []
        #     for j in range(1, count):
        #         _next = strs[j]
        #         if len(_next) == i:
        #             judge_list.append(True)
        #             break
        #         judge_list.append(_next[i] != target)
        #     if any(judge_list):
        #         return first[:i]
        # return first
        pass


if __name__ == '__main__':
    strs1 = ["flower", "flow", "flight"]
    strs2 = ["dog", "racecar", "car"]
    strs3 = ["dog", "dig", "d"]
    strs4 = ["dog", "dog", "dog"]
    s = Solution()
    ret1 = s.longestCommonPrefix(strs1)
    ret2 = s.longestCommonPrefix(strs2)
    ret3 = s.longestCommonPrefix(strs3)
    ret4 = s.longestCommonPrefix(strs4)
    print(ret1)
    print(ret2)
    print(ret3)
    print(ret4)
