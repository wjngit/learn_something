# 剑指 Offer 61. 扑克牌中的顺子
#
# 从若干副扑克牌中随机抽 5 张牌，判断是不是一个顺子，即这5张牌是不是连续的。
# 2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14。
#
# 示例1:
# 输入: [1, 2, 3, 4, 5]
# 输出: True
#
# 示例2:
# 输入: [0, 0, 1, 2, 5]
# 输出: True
#
# 限制：
# 数组长度为 5 数组的数取值为[0, 13].

from typing import List


class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        # # 除0以外不能重复
        # count = {}
        # for i in nums:
        #     if i in count:
        #         count[i] += 1
        #     else:
        #         count[i] = 1
        # for i in count:
        #     if count[i] != 1 and i != 0:
        #         return False
        #
        # nums.sort()
        # max_ = nums[-1]
        # min_ = 0
        # for i in nums:
        #     if i != 0:
        #         min_ = i
        #         break
        # c = max_ - min_
        # if 1 < c < 5:
        #     return True
        #
        # return False

        pass


if __name__ == '__main__':
    l1 = [1, 2, 3, 4, 6]
    l2 = [0, 0, 1, 2, 5]

    s = Solution()
    r1 = s.isStraight(l1)
    r2 = s.isStraight(l2)
    print(r1)
    print(r2)
