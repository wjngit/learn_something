# 34. 在排序数组中查找元素的第一个和最后一个位置
#
# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
# 如果数组中不存在目标值 target，返回 [-1, -1]。
#
# 进阶：你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？
#
# 示例 1：
# 输入：nums = [5,7,7,8,8,10], target = 8
# 输出：[3,4]
#
# 示例 2：
# 输入：nums = [5,7,7,8,8,10], target = 6
# 输出：[-1,-1]
#
# 示例 3：
# 输入：nums = [], target = 0
# 输出：[-1,-1]
#
# 提示：
#     0 <= nums.length <= 10^5
#     -10^9 <= nums[i] <= 10^9
#     nums 是一个非递减数组
#     -10^9 <= target <= 10^9


from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # n = len(nums)
        # low1, high1 = 0, n - 1
        # low2, high2 = 0, n - 1
        # start, end = -1, -1
        # while low1 <= high1:
        #     mid = low1 + (high1 - low1) // 2
        #     if nums[mid] == target:
        #         if mid == 0 or nums[mid - 1] != target:
        #             start = mid
        #             break
        #         else:
        #             high1 = mid - 1
        #     elif nums[mid] > target:
        #         high1 = mid - 1
        #     else:
        #         low1 = mid + 1
        # while low2 <= high2:
        #     mid = low2 + (high2 - low2) // 2
        #     if nums[mid] == target:
        #         if mid == n - 1 or nums[mid + 1] != target:
        #             end = mid
        #             break
        #         else:
        #             low2 = mid + 1
        #     elif nums[mid] < target:
        #         low2 = mid + 1
        #     else:
        #         high2 = mid - 1
        # return [start, end]

        pass


if __name__ == '__main__':
    nums1 = [5, 7, 7, 8, 8, 10]
    target1 = 8
    nums2 = [5, 7, 7, 8, 9, 10]
    target2 = 9
    nums3 = [5, 7, 7, 8, 8, 10]
    target3 = 6
    nums4 = []
    target4 = 0

    s = Solution()
    r1 = s.searchRange(nums1, target1)
    r2 = s.searchRange(nums2, target2)
    r3 = s.searchRange(nums2, target3)
    r4 = s.searchRange(nums3, target4)
    print(r1)
    print(r2)
    print(r3)
    print(r4)
