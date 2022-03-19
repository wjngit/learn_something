# 面试题 16.21. 交换和
#
# 给定两个整数数组，请交换一对数值（每个数组中取一个数值），使得两个数组所有元素的和相等。
# 返回一个数组，第一个元素是第一个数组中要交换的元素，第二个元素是第二个数组中要交换的元素。
# 若有多个答案，返回任意一个均可。若无满足条件的数值，返回空数组。
#
# 示例1:
# 输入: array1 = [4, 1, 2, 1, 1, 2], array2 = [3, 6, 3, 3]
# 输出: [1, 3]
#
# 示例2:
# 输入: array1 = [1, 2, 3], array2 = [4, 5, 6]
# 输出: []
#
# 提示：1 <= array1.length, array2.length <= 100000


from typing import List


class Solution:
    def findSwapValues(self, array1: List[int], array2: List[int]) -> List[int]:
        # sum1 = 0
        # for i in array1:
        #     sum1 += i
        # sum2 = 0
        # temp = set()
        # for j in array2:
        #     sum2 += j
        #     temp.add(j)
        # sum_all = sum2 + sum1
        # if sum_all % 2 == 1:
        #     return []
        # diff = sum_all // 2 - sum1
        # for k in array1:
        #     target = k + diff
        #     if target in temp:
        #         return [k, target]
        # return []

        pass


if __name__ == '__main__':
    array11 = [4, 1, 2, 1, 1, 2]
    array12 = [3, 6, 3, 3]
    array21 = [1, 2, 3]
    array22 = [4, 5, 6]

    array31 = [3, 6, 3, 3]
    array32 = [4, 1, 2, 1, 1, 2]

    s = Solution()
    r3 = s.findSwapValues(array31, array32)
    r1 = s.findSwapValues(array11, array12)
    r2 = s.findSwapValues(array21, array22)
    print(r1)
    print(r2)
    print(r3)
