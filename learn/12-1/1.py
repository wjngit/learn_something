# 面试题 16.24. 数对和
#
# 设计一个算法，找出数组中两数之和为指定值的所有整数对。一个数只能属于一个数对。
#
# 示例 1:
# 输入: nums = [5,6,5], target = 11
# 输出: [[5,6]]
#
# 示例 2:
# 输入: nums = [5,6,5,6], target = 11
# 输出: [[5,6],[5,6]]
#
# 提示：nums.length <= 100000


from typing import List


class Solution:
    def pairSums(self, nums: List[int], target: int) -> List[List[int]]:
        # result = []
        # n = len(nums)
        # if n == 0:
        #     return result
        # nums.sort()
        # i, j = 0, n - 1
        # while i < j:
        #     if nums[i] + nums[j] == target:
        #         result.append([nums[i], nums[j]])
        #         i += 1
        #         j -= 1
        #     elif nums[i] + nums[j] < target:
        #         i += 1
        #     else:
        #         j -= 1
        # return result

        pass


if __name__ == '__main__':
    nums1 = [5, 6, 5]
    target1 = 11
    nums2 = [5, 6, 5, 6]
    target2 = 11

    s = Solution()
    r1 = s.pairSums(nums1, target1)
    r2 = s.pairSums(nums2, target2)
    print(r1)
    print(r2)
