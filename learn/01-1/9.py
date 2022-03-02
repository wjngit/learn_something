# 剑指 Offer 58 - II.左旋转字符串
#
# 字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。
# 请定义一个函数实现字符串左旋转操作的功能。
# 比如，输入字符串"abcdefg"和数字 2，该函数将返回左旋转两位得到的结果"cdefgab"。
#
# 示例1：
# 输入: s = "abcdefg", k = 2
# 输出: "cdefgab"
#
# 示例2：
# 输入: s = "lrloseumgh", k = 6
# 输出: "umghlrlose"
#
# 限制：
# 1 <= k < s.length <= 10000

class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        # temp = s + s[:n]
        # return temp[n:]

        # temp = [""] * len(s)
        # for i in range(n):
        #     temp[len(s) - n + i] = s[i]
        # for i in range(n, len(s)):
        #     temp[i - n] = s[i]
        # return "".join(temp)

        # count = len(s)
        # temp = [""] * count
        # for i in range(n):
        #     temp[count - n + i] = s[i]
        # for j in range(n, count):
        #     temp[j - n] = s[j]
        # return "".join(temp)

        pass


if __name__ == '__main__':
    s1 = "abcdefg"
    k1 = 2
    s2 = "lrloseumgh"
    k2 = 6

    s = Solution()
    r1 = s.reverseLeftWords(s1, k1)
    r2 = s.reverseLeftWords(s2, k2)
    print(r1)
    print(r2)
