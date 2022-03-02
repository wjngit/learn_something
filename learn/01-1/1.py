# 1.两数之和
#
# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target 的那 两个 整数，并返回它们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
# 你可以按任意顺序返回答案。
#
# 示例1：
# 输入：nums = [2, 7, 11, 15], target = 9
# 输出：[0, 1]
# 解释：因为 nums[0] + nums[1] == 9 ，返回[0, 1] 。
#
# 示例2：
# 输入：nums = [3, 2, 4], target = 6
# 输出：[1, 2]
#
# 示例3：
# 输入：nums = [3, 3], target = 6
# 输出：[0, 1]
#
# 提示：
# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# 只会存在一个有效答案
#
# 进阶：你可以想出一个时间复杂度小于 O(n2) 的算法吗？

from typing import List


class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     for index, data in enumerate(nums):
    #         second_data = target - data
    #         for i in range(index + 1, len(nums)):
    #             if nums[i] == second_data:
    #                 return [index, i]
    #     return []

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # temp = {}
        # for index, data in enumerate(nums):
        #     temp[data] = index
        # for index, data1 in enumerate(nums):
        #     second_index = temp.get(target - data1)
        #     if second_index and second_index != index:
        #         return [index, second_index]
        # return []

        pass


if __name__ == '__main__':
    nums1 = [2, 7, 11, 15]
    target1 = 9
    nums2 = [3, 2, 4]
    target2 = 6
    nums3 = [3, 3]
    target3 = 6
    nums4 = [1, 3, 4, 2]
    target4 = 6

    s = Solution()
    r1 = s.twoSum(nums1, target1)
    r2 = s.twoSum(nums2, target2)
    r3 = s.twoSum(nums3, target3)
    r4 = s.twoSum(nums4, target4)
    print(r1)
    print(r2)
    print(r3)
    print(r4)
