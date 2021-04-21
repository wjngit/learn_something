# -*- coding:utf-8 -*-
"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。

示例 1：
输入：s = "()"
输出：true

示例 2：
输入：s = "()[]{}"
输出：true

示例 3：
输入：s = "(]"
输出：false

示例 4：
输入：s = "([)]"
输出：false

示例 5：
输入：s = "{[]}"
输出：true
"""


class Solution(object):
    def isValid(self, s: str) -> bool:
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 != 0:
            return False
        tmp_dict = {")": "(", "]": "[", "}": "{"}
        stack = list()
        for x in s:
            if x in tmp_dict:
                if not stack or stack[-1] != tmp_dict[x]:
                    return False
                stack.pop()
            else:
                stack.append(x)
        return not stack


if __name__ == '__main__':
    s1 = "()"
    s2 = "()[]{}"
    s3 = "(]"
    s4 = "([)]"
    s5 = "{[]}"
    s = Solution()
    ret1 = s.isValid(s1)
    ret2 = s.isValid(s2)
    ret3 = s.isValid(s3)
    ret4 = s.isValid(s4)
    ret5 = s.isValid(s5)
    print(ret1)
    print(ret2)
    print(ret3)
    print(ret4)
    print(ret5)
