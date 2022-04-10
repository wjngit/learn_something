# 53. 最大子数组和
#
# 给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
# 子数组 是数组中的一个连续部分。
#
# 示例 1：
# 输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出：6
# 解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
#
# 示例 2：
# 输入：nums = [1]
# 输出：1
#
# 示例 3：
# 输入：nums = [5,4,-1,7,8]
# 输出：23
#
# 提示：
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
#
# 进阶：如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的 分治法 求解。


from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # if len(nums) == 1:
        #     return nums[0]
        # n = len(nums)
        # totalSum = [0] * n
        # maxCur = [0] * n
        # cursum = 0
        # for i in range(n):
        #     cursum += nums[i]
        #     totalSum[i] = cursum
        # cursum = float("-inf")
        # for i in range(n - 1, -1, -1):
        #     if cursum < totalSum[i]:
        #         cursum = totalSum[i]
        #     maxCur[i] = cursum
        # result = float("-inf")
        # for i in range(n):
        #     if i == 0 and result < maxCur[0]:
        #         result = maxCur[0]
        #     if i != 0 and result < maxCur[i] - totalSum[i - 1]:
        #         result = maxCur[i] - totalSum[i - 1]
        # return result

        pass

        # # 滑动窗口思想
        # n = len(nums)
        # max_sum = float("-inf")
        # total = 0
        # for i in range(n):
        #     if total < 0:
        #         total = 0
        #     total += nums[i]
        #     if total > max_sum:
        #         max_sum = total
        # return max_sum

        pass




if __name__ == '__main__':
    nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    nums2 = [1]
    nums3 = [5, 4, -1, 7, 8]

    s = Solution()
    r1 = s.maxSubArray(nums1)
    r2 = s.maxSubArray(nums2)
    r3 = s.maxSubArray(nums3)
    print(r1)
    print(r2)
    print(r3)
