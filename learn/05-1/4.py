# 35. 搜索插入位置
#
# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
# 请必须使用时间复杂度为 O(log n) 的算法。
#
# 示例 1:
# 输入: nums = [1,3,5,6], target = 5
# 输出: 2
#
# 示例 2:
# 输入: nums = [1,3,5,6], target = 2
# 输出: 1
#
# 示例 3:
# 输入: nums = [1,3,5,6], target = 7
# 输出: 4
#
# 示例 4:
# 输入: nums = [1,3,5,6], target = 0
# 输出: 0
#
# 示例 5:
# 输入: nums = [1], target = 0
# 输出: 0
#
# 提示:
#     1 <= nums.length <= 10^4
#     -10^4 <= nums[i] <= 10^4
#     nums 为无重复元素的升序排列数组
#     -10^4 <= target <= 10^4


from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # n = len(nums)
        # low, high = 0, n - 1
        # while low <= high:
        #     mid = low + (high - low) // 2
        #     if nums[mid] >= target:
        #         if mid == 0 or nums[mid - 1] < target:
        #             return mid
        #         high = mid - 1
        #     else:
        #         low = mid + 1
        # return n

        pass


if __name__ == '__main__':
    nums1 = [1, 3, 5, 6]
    target1 = 5
    nums2 = [1, 3, 5, 6]
    target2 = 2
    nums3 = [1, 3, 5, 6]
    target3 = 7
    nums4 = [1, 3, 5, 6]
    target4 = 0
    nums5 = [1]
    target5 = 0

    s = Solution()
    r1 = s.searchInsert(nums1, target1)
    r2 = s.searchInsert(nums2, target2)
    r3 = s.searchInsert(nums3, target3)
    r4 = s.searchInsert(nums4, target4)
    r5 = s.searchInsert(nums5, target5)
    print(r1)
    print(r2)
    print(r3)
    print(r4)
    print(r5)
