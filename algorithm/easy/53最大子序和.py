# -*- coding:utf-8 -*-
"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例 1：
输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。

示例 2：
输入：nums = [1]
输出：1

示例 3：
输入：nums = [0]
输出：0

示例 4：
输入：nums = [-1]
输出：-1

示例 5：
输入：nums = [-100000]
输出：-100000
"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # temp = nums[0]
        # max_ = temp
        # for i in range(1, len(nums)):
        #     if temp > 0:
        #         temp += nums[i]
        #         max_ = max(max_, temp)
        #
        #     else:
        #         temp = nums[i]
        #         max_ = max(max_, temp)
        # return max_

        pass


if __name__ == '__main__':
    nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    nums2 = [1]
    nums3 = [0]
    nums4 = [-1]
    nums5 = [-100000]
    s = Solution()
    ret1 = s.maxSubArray(nums1)
    ret2 = s.maxSubArray(nums2)
    ret3 = s.maxSubArray(nums3)
    ret4 = s.maxSubArray(nums4)
    ret5 = s.maxSubArray(nums5)
    print(ret1)
    print(ret2)
    print(ret3)
    print(ret4)
    print(ret5)
