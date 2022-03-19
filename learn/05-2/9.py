# 242. 有效的字母异位词
#
# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
# 注意：若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词。
#
# 示例 1:
# 输入: s = "anagram", t = "nagaram"
# 输出: true
#
# 示例 2:
# 输入: s = "rat", t = "car"
# 输出: false
#
# 提示:
#     1 <= s.length, t.length <= 5 * 104
#     s 和 t 仅包含小写字母
#
# 进阶: 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # temp_a_list, temp_b_list = [0] * 26, [0] * 26
        # for i in s:
        #     temp_a_list[ord(i) - ord("a")] += 1
        # for j in t:
        #     temp_b_list[ord(j) - ord("a")] += 1
        # for k in range(26):
        #     if temp_a_list[k] != temp_b_list[k]:
        #         return False
        # return True

        pass


if __name__ == '__main__':
    s1 = "anagram"
    t1 = "nagaram"
    s2 = "rat"
    t2 = "car"

    s = Solution()
    r1 = s.isAnagram(s1, t1)
    r2 = s.isAnagram(s2, t2)
    print(r1)
    print(r2)
