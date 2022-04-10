# 438. 找到字符串中所有字母异位词
#
# 给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
# 异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。
#
# 示例 1:
# 输入: s = "cbaebabacd", p = "abc"
# 输出: [0,6]
# 解释:
# 起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
# 起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。
#
# 示例 2:
# 输入: s = "abab", p = "ab"
# 输出: [0,1,2]
# 解释:
# 起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
# 起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
# 起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。
#
# 提示:
# 1 <= s.length, p.length <= 3 * 104
# s 和 p 仅包含小写字母


from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        #     m, n = len(s), len(p)
        #     if n > m:
        #         return []
        #
        #     counts = [0] * 26
        #     for i in range(n):
        #         counts[ord(p[i]) - ord("a")] += 1
        #
        #     matched = [0] * 26
        #     start_p, end_p = 0, 0
        #     result = []
        #     while end_p < n:
        #         matched[ord(s[end_p]) - ord("a")] += 1
        #         end_p += 1
        #
        #     if self.same(counts, matched):
        #         result.append(start_p)
        #
        #     while end_p < m and start_p < m:
        #         matched[ord(s[start_p]) - ord("a")] -= 1
        #         matched[ord(s[end_p]) - ord("a")] += 1
        #         start_p += 1
        #         end_p += 1
        #         if self.same(counts, matched):
        #             result.append(start_p)
        #     return result
        #
        # def same(self, counts, matched):
        #     for i in range(len(counts)):
        #         if counts[i] != matched[i]:
        #             return False
        #     return True

        pass


if __name__ == '__main__':
    s1 = "cbaebabacd"
    p1 = "abc"
    s2 = "abab"
    p2 = "ab"

    s = Solution()
    r1 = s.findAnagrams(s1, p1)
    r2 = s.findAnagrams(s2, p2)
    print(r1)
    print(r2)
