# -*- coding:utf-8 -*-
"""
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 的那 两个 整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
你可以按任意顺序返回答案。

示例 1：
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

示例 2：
输入：nums = [3,2,4], target = 6
输出：[1,2]

示例 3：
输入：nums = [3,3], target = 6
输出：[0,1]
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # ret_dict = {}
        # for i, num in enumerate(nums):
        #     tmp = target - num
        #     if tmp in ret_dict:
        #         return [ret_dict[tmp], i]
        #     ret_dict[num] = i
        # return []

        pass


if __name__ == '__main__':
    nums1 = [2, 7, 11, 15]
    target1 = 9
    nums2 = [3, 2, 4]
    target2 = 6
    nums3 = [3, 3]
    target3 = 6
    s = Solution()
    ret1 = s.twoSum(nums1, target1)
    print(ret1)
    ret2 = s.twoSum(nums2, target2)
    print(ret2)
    ret3 = s.twoSum(nums3, target3)
    print(ret3)
