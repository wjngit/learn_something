# 58.最后一个单词的长度
#
# 给你一个字符串 s，由若干单词组成，单词前后用一些空格字符隔开。返回字符串中最后一个单词的长度。
# 单词 是指仅由字母组成、不包含任何空格字符的最大子字符串。
#
# 示例1：
# 输入：s = "Hello World"
# 输出：5
#
# 示例2：
# 输入：s = "   fly me   to   the moon  "
# 输出：4
#
# 示例3：
# 输入：s = "luffy is still joyboy"
# 输出：6
#
# 提示：
# 1 <= s.length <= 104
# s 仅有英文字母和空格 ' ' 组成
# s 中至少存在一个单词

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # return len([i for i in s.split(" ") if i][-1])

        # i = len(s) - 1
        # j = 0
        # while i >= 0:
        #     if s[i] != " ":
        #         j += 1
        #     else:
        #         if j != 0:
        #             return j
        #     i -= 1
        # return j

        pass


if __name__ == '__main__':
    s1 = "Hello World"
    s2 = "   fly me   to   the moon  "
    s3 = "luffy is still joyboy"
    s4 = " "

    s = Solution()
    r1 = s.lengthOfLastWord(s1)
    r2 = s.lengthOfLastWord(s2)
    r3 = s.lengthOfLastWord(s3)
    r4 = s.lengthOfLastWord(s4)
    print(r1)
    print(r2)
    print(r3)
    print(r4)
