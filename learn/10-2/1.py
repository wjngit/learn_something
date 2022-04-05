# 416. 分割等和子集
#
# 给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
#
# 示例 1：
# 输入：nums = [1,5,11,5]
# 输出：true
# 解释：数组可以分割成 [1, 5, 5] 和 [11] 。
#
# 示例 2：
# 输入：nums = [1,2,3,5]
# 输出：false
# 解释：数组不能分割成两个元素和相等的子集。
#
# 提示：
# 1 <= nums.length <= 200
# 1 <= nums[i] <= 100


from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # n = len(nums)
        # target = sum(nums)
        # if target % 2 == 1:
        #     return False
        # target = target // 2
        # dp = [[False] * (target + 1) for _ in range(n)]
        # dp[0][0] = True
        # if nums[0] <= target:
        #     dp[0][nums[0]] = True
        # for i in range(1, n):
        #     for j in range(target + 1):
        #         # if j - nums[i] >= 0:
        #         #     dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i]]
        #         # else:
        #         #     dp[i][j] = dp[i - 1][j]
        #         if dp[i - 1][j] is True or (j - nums[i] >= 0 and dp[i - 1][j - nums[i]] is True):
        #             dp[i][j] = True
        # return dp[n - 1][target]

        pass


if __name__ == '__main__':
    nums1 = [1, 5, 11, 5]
    nums2 = [1, 2, 3, 5]

    s1 = Solution()
    s2 = Solution()
    r1 = s1.canPartition(nums1)
    r2 = s2.canPartition(nums2)
    print(r1)
    print(r2)
