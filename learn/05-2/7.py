# 面试题 01.02. 判定是否互为字符重排
#
# 给定两个字符串 s1 和 s2，请编写一个程序，确定其中一个字符串的字符重新排列后，能否变成另一个字符串。
#
# 示例 1：
# 输入: s1 = "abc", s2 = "bca"
# 输出: true
#
# 示例 2：
# 输入: s1 = "abc", s2 = "bad"
# 输出: false
#
# 说明：
#     0 <= len(s1) <= 100
#     0 <= len(s2) <= 100


class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        # if len(s1) != len(s2):
        #     return False
        # s1_l = list(s1)
        # s2_l = list(s2)
        # s1_l.sort()
        # s2_l.sort()
        # for i in range(len(s1_l)):
        #     if s1_l[i] != s2_l[i]:
        #         return False
        # return True

        pass

        # s1_dict = {}
        # for i in s1:
        #     if i in s1_dict:
        #         s1_dict[i] += 1
        #     else:
        #         s1_dict[i] = 1
        # for j in s2:
        #     if j in s1 and s1_dict[j] >= 1:
        #         s1_dict[j] -= 1
        #     else:
        #         return False
        # for k in s1_dict:
        #     if s1_dict[k] != 0:
        #         return False
        # return True

        pass


if __name__ == '__main__':
    s11 = "abc"
    s12 = "bca"
    s21 = "abc"
    s22 = "bad"

    s = Solution()
    r1 = s.CheckPermutation(s11, s12)
    r2 = s.CheckPermutation(s21, s22)
    print(r1)
    print(r2)
