# -*- coding:utf-8 -*-
"""
实现 strStr() 函数。
给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。如果不存在，则返回 -1 。

说明：
当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与 C 语言的 strstr() 以及 Java 的 indexOf() 定义相符。

示例 1：
输入：haystack = "hello", needle = "ll"
输出：2

示例 2：
输入：haystack = "aaaaa", needle = "bba"
输出：-1

示例 3：
输入：haystack = "", needle = ""
输出：0
"""


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # if needle == "" or needle == haystack:
        #     return 0
        # elif len(needle) > len(haystack):
        #     return -1
        # else:
        #     for i in range(len(haystack)):
        #         if haystack[i] == needle[0]:
        #             n = len(needle)
        #             if haystack[i:i + n] == needle:
        #                 return i
        #     return -1

        pass


if __name__ == '__main__':
    haystack1, needle1 = 'hello', 'll'
    haystack2, needle2 = 'aaaaa', 'bba'
    haystack3, needle3 = 'abc', 'c'
    haystack4, needle4 = '', 'c'
    haystack5, needle5 = '', ''
    s = Solution()
    ret1 = s.strStr(haystack1, needle1)
    ret2 = s.strStr(haystack2, needle2)
    ret3 = s.strStr(haystack3, needle3)
    ret4 = s.strStr(haystack4, needle4)
    ret5 = s.strStr(haystack5, needle5)
    print(ret1)
    print(ret2)
    print(ret3)
    print(ret4)
    print(ret5)
