# 55. 跳跃游戏
#
# 给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
# 判断你是否能够到达最后一个下标。
#
# 示例1：
# 输入：nums = [2, 3, 1, 1, 4]
# 输出：true
# 解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。
#
# 示例2：
# 输入：nums = [3, 2, 1, 0, 4]
# 输出：false
# 解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。
#
# 提示：
#     1 <= nums.length <= 3 * 104
#     0 <= nums[i] <= 105

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # reach_max = 0
        # for i in range(len(nums)):
        #     if i > reach_max:
        #         return False
        #     if nums[i] + i > reach_max:
        #         reach_max = nums[i] + i
        #     if reach_max >= len(nums) - 1:
        #         return True
        # return False

        pass

        # temp = [1] + [0] * (len(nums) - 1)
        # for i in range(len(nums)):
        #     if temp[i] != 1:
        #         return False
        #     for j in range(nums[i]):
        #         target = i + j + 1
        #         if target >= len(nums) - 1:
        #             return True
        #         temp[i + j + 1] = 1
        # return temp[-1] == 1

        pass


if __name__ == '__main__':
    nums1 = [2, 3, 1, 1, 4]
    nums2 = [3, 2, 1, 0, 4]
    nums3 = [0]

    s = Solution()
    r1 = s.canJump(nums1)
    r2 = s.canJump(nums2)
    r3 = s.canJump(nums3)
    print(r1)
    print(r2)
    print(r3)
