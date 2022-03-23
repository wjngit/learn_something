# 面试题 16.26. 计算器
#
# 给定一个包含正整数、加(+)、减(-)、乘(*)、除(/)的算数表达式(括号除外)，计算其结果。
# 表达式仅包含非负整数，+， - ，*，/ 四种运算符和空格  。 整数除法仅保留整数部分。
#
# 示例 1:
# 输入: "3+2*2"
# 输出: 7
#
# 示例 2:
# 输入: " 3/2 "
# 输出: 1
#
# 示例 3:
# 输入: " 3+5 / 2 "
# 输出: 5
#
# 说明：
#     你可以假设所给定的表达式都是有效的。
#     请不要使用内置的库函数 eval。


class Solution:
    def calculate(self, s: str) -> int:
        #     data = []
        #     option = []
        #     n = len(s)
        #     i = 0
        #     while i < n:
        #         c = s[i]
        #         if c == " ":
        #             i += 1
        #         elif c.isdigit():
        #             num = 0
        #             while i < n and s[i].isdigit():
        #                 num = num * 10 + int(s[i])
        #                 i += 1
        #             data.append(num)
        #         else:
        #             if not option or self.aaa(option[-1], c):
        #                 option.append(c)
        #             else:
        #                 while option and not self.aaa(option[-1], c):
        #                     self.ccc(option, data)
        #                 option.append(c)
        #             i += 1
        #     while option:
        #         self.ccc(option, data)
        #     return data.pop()
        #
        # def aaa(self, opt, c):
        #     if c in ["*", "/"] and opt in ["+", "-"]:
        #         return True
        #     return False
        #
        # def bbb(self, opt, num1, num2):
        #     if opt == "+":
        #         return num1 + num2
        #     if opt == "-":
        #         return num1 - num2
        #     if opt == "*":
        #         return num1 * num2
        #     if opt == "/":
        #         return num1 // num2
        #
        # def ccc(self, option, data):
        #     num2 = data.pop()
        #     num1 = data.pop()
        #     opt = option.pop()
        #     ret = self.bbb(opt, num1, num2)
        #     data.append(ret)

        pass


if __name__ == '__main__':
    s1 = "3+2*2"
    s2 = " 3/2 "
    s3 = " 3+5 / 2 "
    s4 = "43"

    s = Solution()
    r1 = s.calculate(s1)
    r2 = s.calculate(s2)
    r3 = s.calculate(s3)
    r4 = s.calculate(s4)
    print(r1)
    print(r2)
    print(r3)
    print(r4)
