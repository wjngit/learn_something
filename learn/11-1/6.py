# 139. 单词拆分
#
# 给你一个字符串 s 和一个字符串列表 wordDict 作为字典。请你判断是否可以利用字典中出现的单词拼接出 s 。
# 注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。
#
# 示例 1：
# 输入: s = "leetcode", wordDict = ["leet", "code"]
# 输出: true
# 解释: 返回 true 因为 "leetcode" 可以由 "leet" 和 "code" 拼接成。
#
# 示例 2：
# 输入: s = "applepenapple", wordDict = ["apple", "pen"]
# 输出: true
# 解释: 返回 true 因为 "applepenapple" 可以由 "apple" "pen" "apple" 拼接成。
#      注意，你可以重复使用字典中的单词。
#
# 示例 3：
# 输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出: false
#
# 提示：
# 1 <= s.length <= 300
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 20
# s 和 wordDict[i] 仅有小写英文字母组成
# wordDict 中的所有字符串 互不相同


from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for word in wordDict:
                lenght = len(word)
                startp = i - lenght
                if startp >= 0 and s.startswith(word, startp) and dp[i - lenght]:
                    dp[i] = True
                    break
        return dp[n]


if __name__ == '__main__':
    s1 = "leetcode"
    wordDict1 = ["leet", "code"]
    s2 = "applepenapple"
    wordDict2 = ["apple", "pen"]
    s3 = "catsandog"
    wordDict3 = ["cats", "dog", "sand", "and", "cat"]

    s = Solution()
    r1 = s.wordBreak(s1, wordDict1)
    r2 = s.wordBreak(s2, wordDict2)
    r3 = s.wordBreak(s3, wordDict3)
    print(r1)
    print(r2)
    print(r3)
