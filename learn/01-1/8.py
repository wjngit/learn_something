# 剑指 Offer 05. 替换空格
# 请实现一个函数，把字符串 s 中的每个空格替换成 "%20"。
#
# 示例1：
# 输入：s = "We are happy."
# 输出："We%20are%20happy."
#
# 限制：
# 0 <= s 的长度 <= 10000

class Solution:
    def replaceSpace(self, s: str) -> str:
        # temp = ""
        # for i in s:
        #     if i != " ":
        #         temp += i
        #     else:
        #         temp += "%20"
        # return temp

        pass


if __name__ == '__main__':
    s1 = "We are happy."

    s = Solution()
    r1 = s.replaceSpace(s1)
    print(r1)
