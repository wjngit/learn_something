# 剑指 Offer 67. 把字符串转换成整数
#
# 写一个函数 StrToInt，实现把字符串转换成整数这个功能。不能使用 atoi 或者其他类似的库函数。
# 首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。
# 当我们寻找到的第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字组合起来，作为该整数的正负号；
# 假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数。
# 该字符串除了有效的整数部分之后也可能会存在多余的字符，这些字符可以被忽略，它们对于函数不应该造成影响。
# 注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，
# 则你的函数不需要进行转换。
# 在任何情况下，若函数不能进行有效的转换时，请返回 0。
#
# 说明：
# 假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为[−2**31, 2**31 − 1]。
# 如果数值超过这个范围，请返回 INT_MAX(2**31 − 1) 或 INT_MIN(−2**31) 。
#
# 示例1:
# 输入: "42"
# 输出: 42
#
# 示例2:
# 输入: "   -42"
# 输出: -42
# 解释: 第一个非空白字符为 '-', 它是一个负号。
# 我们尽可能将负号与后面所有连续出现的数字组合起来，最后得到 -42 。
#
# 示例3:
# 输入: "4193 with words"
# 输出: 4193
# 解释: 转换截止于数字'3' ，因为它的下一个字符不为数字。
#
# 示例4:
# 输入: "words and 987"
# 输出: 0
# 解释: 第一个非空字符是'w', 但它不是数字或正、负号。
# 因此无法执行有效的转换。
#
# 示例5:
# 输入: "-91283472332"
# 输出: -2147483648
# 解释: 数字"-91283472332"超过 32 位有符号整数范围。因此返回 INT_MIN(−231) 。

class Solution:
    def strToInt(self, str: str) -> int:
        # str_list = [i for i in str]
        # count = len(str_list)
        # if count == 0:
        #     return 0
        #
        # i = 0
        # while i < count:
        #     if str_list[i] == " ":
        #         i += 1
        #     else:
        #         break
        # if i == count:
        #     return 0
        #
        # sign = 1
        # c = str_list[i]
        # if c == "-":
        #     sign = -1
        #     i += 1
        # if c == "+":
        #     i += 1
        #
        # high = 214748364
        # result = 0
        # while i < count and "0" <= str_list[i] <= "9":
        #     d = int(str_list[i])
        #     if result > high:
        #         if sign == 1:
        #             return 2 ** 31 - 1
        #         else:
        #             return -2 ** 31
        #     if result == high:
        #         if sign == 1 and d > 7:
        #             return 2 ** 31 - 1
        #         if sign == -1 and d > 8:
        #             return -2 ** 31
        #     result = result * 10 + d
        #     i += 1
        # return result * sign

        pass


if __name__ == '__main__':
    s1 = "42"
    s2 = "   -42"
    s3 = "4193 with words"
    s4 = "words and 987"
    s5 = "-91283472332"

    s = Solution()
    r1 = s.strToInt(s1)
    r2 = s.strToInt(s2)
    r3 = s.strToInt(s3)
    r4 = s.strToInt(s4)
    r5 = s.strToInt(s5)
    print(r1)
    print(r2)
    print(r3)
    print(r4)
    print(r5)
