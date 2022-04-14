# 300. 最长递增子序列
#
# 给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
# 子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。
#
# 示例 1：
# 输入：nums = [10,9,2,5,3,7,101,18]
# 输出：4
# 解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
#
# 示例 2：
# 输入：nums = [0,1,0,3,2,3]
# 输出：4
#
# 示例 3：
# 输入：nums = [7,7,7,7,7,7,7]
# 输出：1
#
# 提示：
# 1 <= nums.length <= 2500
# -104 <= nums[i] <= 104
#
# 进阶：你能将算法的时间复杂度降低到 O(n log(n)) 吗?


from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # n = len(nums)
        # 以nums[i]为结尾的最长递增子序列
        # dp = [0] * n
        # dp[0] = 1
        # for i in range(1, n):
        #     dp[i] = 1
        #     for j in range(i):
        #         if nums[i] > nums[j]:
        #             dp[i] = max(dp[i], dp[j] + 1)
        # result = 0
        # for i in range(n):
        #     if dp[i] > result:
        #         result = dp[i]
        # return result

        pass

        #     n = len(nums)
        #     listToMinV = [float("inf")] * (n + 1)
        #     k = 0
        #     dp = [0] * n
        #     for i in range(n):
        #         length = self.bsearch(listToMinV, k, nums[i])
        #         if length == -1:
        #             dp[i] = 1
        #         else:
        #             dp[i] = length + 1
        #         if dp[i] > k:
        #             k = dp[i]
        #             listToMinV[dp[i]] = nums[i]
        #         elif listToMinV[dp[i]] > nums[i]:
        #             listToMinV[dp[i]] = nums[i]
        #     result = 0
        #     for i in range(n):
        #         if dp[i] > result:
        #             result = dp[i]
        #     return result
        #
        # def bsearch(self, a, k, target):
        #     low = 1
        #     high = k
        #     while low <= high:
        #         mid = (low + high) // 2
        #         if a[mid] < target:
        #             if mid == k or a[mid + 1] >= target:
        #                 return mid
        #             else:
        #                 low = mid + 1
        #         else:
        #             high = mid - 1
        #     return -1

        pass


if __name__ == '__main__':
    nums1 = [10, 9, 2, 5, 3, 7, 101, 18]
    nums2 = [0, 1, 0, 3, 2, 3]
    nums3 = [7, 7, 7, 7, 7, 7, 7]

    s = Solution()
    r1 = s.lengthOfLIS(nums1)
    r2 = s.lengthOfLIS(nums2)
    r3 = s.lengthOfLIS(nums3)
    print(r1)
    print(r2)
    print(r3)
