# 131. 分割回文串
#
# 给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。
# 回文串 是正着读和反着读都一样的字符串。
#
# 示例 1：
# 输入：s = "aab"
# 输出：[["a","a","b"],["aa","b"]]
#
# 示例 2：
# 输入：s = "a"
# 输出：[["a"]]
#
# 提示：
# 1 <= s.length <= 16
# s 仅由小写英文字母组成


from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        #     self.backtrack(s, 0, [])
        #     return self.result
        #
        # def __init__(self):
        #     self.result = []
        #
        # def backtrack(self, s, k, path):
        #     if k == len(s):
        #         self.result.append(path[:])
        #         return
        #     for end in range(k, len(s)):
        #         if self.ispalindrome(s, k, end):
        #             path.append(s[k:end + 1])
        #             self.backtrack(s, end + 1, path)
        #             path.pop()
        #
        # def ispalindrome(self, s, p, r):
        #     i = p
        #     j = r
        #     while i <= j:
        #         if s[i] != s[j]:
        #             return False
        #         i += 1
        #         j -= 1
        #     return True

        pass


if __name__ == '__main__':
    s1s = "aab"
    s2s = "a"

    s1 = Solution()
    s2 = Solution()
    r1 = s1.partition(s1s)
    r2 = s2.partition(s2s)
    print(r1)
    print(r2)
