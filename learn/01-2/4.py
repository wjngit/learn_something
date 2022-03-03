# 面试题 01.05.一次编辑
#
# 字符串有三种编辑操作: 插入一个字符、删除一个字符或者替换一个字符。
# 给定两个字符串，编写一个函数判定它们是否只需要一次(或者零次)编辑。
#
# 示例1:
# 输入:
#     first = "pale"
#     second = "ple"
# 输出: True
#
# 示例2:
# 输入:
#     first = "pales"
#     second = "pal"
# 输出: False

class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        # f_len, s_len = len(first), len(second)
        # if abs(f_len - s_len) > 1:
        #     return False
        # i, j = 0, 0
        # while i < f_len and j < s_len and first[i] == second[j]:
        #     i += 1
        #     j += 1
        # if f_len == s_len:
        #     i += 1
        #     j += 1
        # elif f_len > s_len:
        #     i += 1
        # else:
        #     j += 1
        # while i < f_len and j < s_len:
        #     if first[i] != second[j]:
        #         return False
        #     i += 1
        #     j += 1
        # return True

        pass


if __name__ == '__main__':
    first1 = "pale"
    second1 = "ple"
    first2 = "pales"
    second2 = "pal"
    first3 = ""
    second3 = "a"
    first4 = "a"
    second4 = "ab"

    s = Solution()
    r1 = s.oneEditAway(first1, second1)
    r2 = s.oneEditAway(first2, second2)
    r3 = s.oneEditAway(first3, second3)
    r4 = s.oneEditAway(first4, second4)
    print(r1)
    print(r2)
    print(r3)
    print(r4)
