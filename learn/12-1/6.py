# 剑指 Offer 48. 最长不含重复字符的子字符串
#
# 请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。
#
# 示例 1:
# 输入: "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
#
# 示例 2:
# 输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
#
# 示例 3:
# 输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
#
# 提示：s.length <= 40000


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        p, q = 0, 0
        record = set()
        max_len = 0
        while q < n:
            c = s[q]
            if c not in record:
                record.add(c)
                q += 1
                if q - p > max_len:
                    max_len = q - p
                continue
            while c in record:
                record.remove(s[p])
                p += 1
        return max_len


if __name__ == '__main__':
    s1 = "abcabcbb"
    s2 = "bbbbb"
    s3 = "pwwkew"

    s = Solution()
    r1 = s.lengthOfLongestSubstring(s1)
    r2 = s.lengthOfLongestSubstring(s2)
    r3 = s.lengthOfLongestSubstring(s3)
    print(r1)
    print(r2)
    print(r3)
