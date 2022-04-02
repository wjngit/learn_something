# 面试题 17.22. 单词转换
#
# 给定字典中的两个词，长度相等。写一个方法，把一个词转换成另一个词， 但是一次只能改变一个字符。每一步得到的新词都必须能在字典中找到。
# 编写一个程序，返回一个可能的转换序列。如有多个可能的转换序列，你可以返回任何一个。
#
# 示例 1:
# 输入:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
# 输出:
# ["hit","hot","dot","lot","log","cog"]
#
# 示例 2:
# 输入:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
# 输出: []
#
# 解释: endWord "cog" 不在字典中，所以不存在符合要求的转换序列。


from typing import List


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[str]:
        #     self.dfs(beginWord, endWord, [], wordList)
        #     return self.result
        #
        # def __init__(self):
        #     self.visited = set()
        #     self.found = False
        #     self.result = []
        #
        # def dfs(self, cur, end, path, word_list):
        #     if self.found:
        #         return
        #     path.append(cur)
        #     self.visited.add(cur)
        #     if cur == end:
        #         self.result.extend(path)
        #         self.found = True
        #         return
        #     for i in range(len(word_list)):
        #         next_word = word_list[i]
        #         if next_word in self.visited or not self.is_valid_change(cur, next_word):
        #             continue
        #         self.dfs(next_word, end, path, word_list)
        #     path.pop()
        #
        # @staticmethod
        # def is_valid_change(word1, word2):
        #     diff = 0
        #     for i in range(len(word1)):
        #         if word1[i] != word2[i]:
        #             diff += 1
        #     return diff == 1

        pass


if __name__ == '__main__':
    beginWord1 = "hit"
    endWord1 = "cog"
    wordList1 = ["hot", "dot", "dog", "lot", "log", "cog"]
    beginWord2 = "hit"
    endWord2 = "cog"
    wordList2 = ["hot", "dot", "dog", "lot", "log"]

    s1 = Solution()
    s2 = Solution()
    r1 = s1.findLadders(beginWord1, endWord1, wordList1)
    r2 = s2.findLadders(beginWord2, endWord2, wordList2)
    print(r1)
    print(r2)
