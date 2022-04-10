# 面试题 17.11. 单词距离
#
# 有个内含单词的超大文本文件，给定任意两个单词，找出在这个文件中这两个单词的最短距离(相隔单词数)。
# 如果寻找过程在这个文件中会重复多次，而每次寻找的单词不同，你能对此优化吗?
#
# 示例：
# 输入：words = ["I","am","a","student","from","a","university","in","a","city"], word1 = "a", word2 = "student"
# 输出：1
#
# 提示：words.length <= 100000


from typing import List


class Solution:
    def findClosest(self, words: List[str], word1: str, word2: str) -> int:
        # w1ps, w2ps = [], []
        # for i in range(len(words)):
        #     if words[i] == word1:
        #         w1ps.append(i)
        #     elif words[i] == word2:
        #         w2ps.append(i)
        # p1, p2 = 0, 0
        # temp = float("inf")
        # while p1 < len(w1ps) and p2 < len(w2ps):
        #     pos1, pos2 = w1ps[p1], w2ps[p2]
        #     if pos1 > pos2:
        #         temp = min(temp, pos1 - pos2)
        #         p2 += 1
        #     else:
        #         temp = min(temp, pos2 - pos1)
        #         p1 += 1
        # return temp

        pass


if __name__ == '__main__':
    words = ["I", "am", "a", "student", "from", "a", "university", "in", "a", "city"]
    word1 = "a"
    word2 = "student"

    s = Solution()
    r = s.findClosest(words, word1, word2)
    print(r)
