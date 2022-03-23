# 772. 基本计算器 III
#
# 给定一个包含正整数、加(+)、减(-)、乘(*)、除(/)的算数表达式(括号不除外)，计算其结果。
# 表达式包含非负整数，+，-，*，/，(，) 六种运算符和空格  。 整数除法仅保留整数部分。
#
# 示例 1:
# 输入: "6-4/2"
# 输出: 4
#
# 示例 2:
# 输入: "(2+6*3+5-(3*14/7+2)*5)+3"
# 输出: -12
#
# 示例 3:
# 输入: "2*(5+5*2)/3+(6/2+8)"
# 输出: 21

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
        #         elif c == "(":
        #             option.append(c)
        #             i += 1
        #         elif c == ")":
        #             while option and not self.aaa(option[-1], c):
        #                 self.ccc(option, data)
        #             option.pop()
        #             i += 1
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
        #     if opt == "(":
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
    s2 = "6-4/2"
    s3 = "(2+6*3+5-(3*14/7+2)*5)+3"
    s4 = "2*(5+5*2)/3+(6/2+8)"

    s = Solution()
    r3 = s.calculate(s3)
    r1 = s.calculate(s1)
    r2 = s.calculate(s2)
    r4 = s.calculate(s4)
    print(r1)
    print(r2)
    print(r3)
    print(r4)
