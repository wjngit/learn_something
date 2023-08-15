# 20. 有效的括号
#
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
# 有效字符串需满足：
#     左括号必须用相同类型的右括号闭合。
#     左括号必须以正确的顺序闭合。
#
# 示例 1：
# 输入：s = "()"
# 输出：true
#
# 示例 2：
# 输入：s = "()[]{}"
# 输出：true
#
# 示例 3：
# 输入：s = "(]"
# 输出：false
#
# 示例 4：
# 输入：s = "([)]"
# 输出：false
#
# 示例 5：
# 输入：s = "{[]}"
# 输出：true
#
# 提示：
#     1 <= s.length <= 104
#     s 仅由括号 '()[]{}' 组成


class Solution:
    def isValid(self, s: str) -> bool:
        # stack = []
        # in_data = ["(", "[", "{"]
        # temp_dict = {")": "(", "]": "[", "}": "{"}
        # for i in s:
        #     if i in in_data:
        #         stack.append(i)
        #         continue
        #     if not stack:
        #         return False
        #     if temp_dict[i] != stack[-1]:
        #         return False
        #     stack.pop()
        # if stack:
        #     return False
        # return True

        pass

        temp = {')': '(', ']': '[', '}': '{'}
        stack = []
        for c in s:
            if not stack or c not in temp:
                stack.append(c)
            else:
                if stack[-1] == temp[c]:
                    stack.pop()
                else:
                    stack.append(c)
        return not stack


if __name__ == '__main__':
    s1 = "()"
    s2 = "()[]{}"
    s3 = "(]"
    s4 = "([)]"
    s5 = "{[]}"
    s6 = "{"
    s7 = "]"

    s = Solution()
    r1 = s.isValid(s1)
    r2 = s.isValid(s2)
    r3 = s.isValid(s3)
    r4 = s.isValid(s4)
    r5 = s.isValid(s5)
    r6 = s.isValid(s6)
    r7 = s.isValid(s7)
    print(r1)
    print(r2)
    print(r3)
    print(r4)
    print(r5)
    print(r6)
    print(r7)
