# -*- coding:utf-8 -*-
"""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
你可以假设数组中无重复元素。

示例 1:
输入: [1,3,5,6], 5
输出: 2

示例 2:
输入: [1,3,5,6], 2
输出: 1

示例 3:
输入: [1,3,5,6], 7
输出: 4

示例 4:
输入: [1,3,5,6], 0
输出: 0
"""


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # left, right = 0, len(nums) - 1
        # while left <= right:
        #     mid = left + (right - left) // 2
        #     if nums[mid] == target:
        #         return mid
        #     elif nums[mid] < target:
        #         left = mid + 1
        #     else:
        #         right = mid - 1
        # return left

        pass


if __name__ == '__main__':
    nums1, target1 = [1, 3, 5, 6], 5
    nums2, target2 = [1, 3, 5, 6], 2
    nums3, target3 = [1, 3, 5, 6], 7
    nums4, target4 = [1, 3, 5, 6], 0
    s = Solution()
    ret1 = s.searchInsert(nums1, target1)
    ret2 = s.searchInsert(nums2, target2)
    ret3 = s.searchInsert(nums3, target3)
    ret4 = s.searchInsert(nums4, target4)
    print(ret1)
    print(ret2)
    print(ret3)
    print(ret4)
