# 面试题 10.05. 稀疏数组搜索
#
# 稀疏数组搜索。有个排好序的字符串数组，其中散布着一些空字符串，编写一种方法，找出给定字符串的位置。
#
# 示例1:
#  输入: words = ["at", "", "", "", "ball", "", "", "car", "", "","dad", "", ""], s = "ta"
#  输出：-1
#  说明: 不存在返回-1。
#
# 示例2:
#  输入：words = ["at", "", "", "", "ball", "", "", "car", "", "","dad", "", ""], s = "ball"
#  输出：4
#
# 提示:words的长度在[1, 1000000]之间


from typing import List


class Solution:
    def findString(self, words: List[str], s: str) -> int:
        # n = len(words)
        # low, high = 0, n - 1
        # while low <= high:
        #     mid = low + (high - low) // 2
        #     if words[mid] == s:
        #         return mid
        #     elif words[mid] == "":
        #         # 左侧缩小范围
        #         if words[low] == s:
        #             return low
        #         low += 1
        #     elif words[mid] > s:
        #         high = mid - 1
        #     else:
        #         low = mid + 1
        # return -1

        pass


if __name__ == '__main__':
    words1 = ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]
    s1 = "ta"
    words2 = ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]
    s2 = "ball"

    s = Solution()
    r1 = s.findString(words1, s1)
    r2 = s.findString(words2, s2)
    print(r1)
    print(r2)
