# 76. 最小覆盖子串
#
# 给你一个字符串 s 、一个字符串 t 。
# 返回 s 中涵盖 t 所有字符的最小子串。
# 如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
# 注意：
#     对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
#     如果 s 中存在这样的子串，我们保证它是唯一的答案。
#
# 示例 1：
# 输入：s = "ADOBECODEBANC", t = "ABC"
# 输出："BANC"
#
# 示例 2：
# 输入：s = "a", t = "a"
# 输出："a"
#
# 示例 3:
# 输入: s = "a", t = "aa"
# 输出: ""
# 解释: t 中两个字符 'a' 均应包含在 s 的子串中，
# 因此没有符合条件的子字符串，返回空字符串。
#
# 提示：
# 1 <= s.length, t.length <= 105
# s 和 t 由英文字母组成
#
# 进阶：你能设计一个在 o(n) 时间内解决此问题的算法吗？


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        minWSize = float("inf")
        minWStart = -1
        minWEnd = -1
        tmap = dict()
        wmap = dict()
        for i in range(len(t)):
            count = 1
            if t[i] in tmap:
                count += tmap[t[i]]
            tmap[t[i]] = count
        n = len(s)
        l = 0
        r = -1
        while l < n and r < n:
            while not self.match(wmap, tmap):
                r += 1
                if r > n - 1:
                    break
                c = s[r]
                if c in tmap:
                    count = 1
                    if c in wmap:
                        count += wmap[c]
                    wmap[c] = count
            if self.match(wmap, tmap):
                if minWSize > r - l + 1:
                    minWSize = r - l + 1
                    minWStart = l
                    minWEnd = r
                c = s[l]
                if c in tmap:
                    count = wmap[c]
                    if count - 1 == 0:
                        wmap.pop(c)
                    else:
                        wmap[c] -= 1
                l += 1
        if minWStart == -1:
            return ""
        return s[minWStart:minWEnd + 1]

    def match(self, wmap, tmap):
        for key, val in tmap.items():
            if key not in wmap:
                return False
            if val > wmap[key]:
                return False
        return True


if __name__ == '__main__':
    s1 = "ADOBECODEBANC"
    t1 = "ABC"
    s2 = "a"
    t2 = "a"
    s3 = "a"
    t3 = "aa"

    s = Solution()
    r1 = s.minWindow(s1, t1)
    r2 = s.minWindow(s2, t2)
    r3 = s.minWindow(s3, t3)
    print(r1)
    print(r2)
    print(r3)
