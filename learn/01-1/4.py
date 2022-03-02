# 剑指 Offer 58 - I.翻转单词顺序
#
# 输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。
# 为简单起见，标点符号和普通字母一样处理。
# 例如输入字符串"I am a student. "，则输出"student. a am I"。
#
# 示例1：
# 输入: "the sky is blue"
# 输出: "blue is sky the"
#
# 示例2：
# 输入: "  hello world!  "
# 输出: "world! hello"
# 解释: 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
#
# 示例3：
# 输入: "a good   example"
# 输出: "example good a"
# 解释: 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
#
# 说明：
# 无空格字符构成一个单词。
# 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
# 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。

class Solution:
    def reverseWords(self, s: str) -> str:
        # one_word = ""
        # temp_list = []
        # for i in range(len(s)):
        #     temp_str = s[i]
        #     if temp_str != " ":
        #         one_word += temp_str
        #         if i + 1 == len(s):
        #             temp_list.append(one_word)
        #     else:
        #         if one_word:
        #             temp_list.append(one_word)
        #             one_word = ""
        # x, y = 0, len(temp_list) - 1
        # while x < y:
        #     temp = temp_list[x]
        #     temp_list[x] = temp_list[y]
        #     temp_list[y] = temp
        #     x += 1
        #     y -= 1
        # return " ".join(temp_list)

        pass


if __name__ == '__main__':
    s1 = "the sky is blue"
    s2 = "  hello world!  "
    s3 = "a good   example"

    s = Solution()
    r1 = s.reverseWords(s1)
    r2 = s.reverseWords(s2)
    r3 = s.reverseWords(s3)
    print(r1)
    print(r2)
    print(r3)
