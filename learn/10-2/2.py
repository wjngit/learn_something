# 494. 目标和
#
# 给你一个整数数组 nums 和一个整数 target 。
# 向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ：
# 例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。
# 返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。
#
# 示例 1：
# 输入：nums = [1,1,1,1,1], target = 3
# 输出：5
# 解释：一共有 5 种方法让最终目标和为 3 。
# -1 + 1 + 1 + 1 + 1 = 3
# +1 - 1 + 1 + 1 + 1 = 3
# +1 + 1 - 1 + 1 + 1 = 3
# +1 + 1 + 1 - 1 + 1 = 3
# +1 + 1 + 1 + 1 - 1 = 3
#
# 示例 2：
# 输入：nums = [1], target = 1
# 输出：1
#
# 提示：
# 1 <= nums.length <= 20
# 0 <= nums[i] <= 1000
# 0 <= sum(nums[i]) <= 1000
# -1000 <= target <= 1000


from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # if target > 1000 or target < -1000:
        #     return 0
        # n = len(nums)
        # offset = 1000
        # w = 2000
        # dp = [[0] * (w + 1) for _ in range(n)]
        # dp[0][offset - nums[0]] += 1
        # dp[0][offset + nums[0]] += 1
        # for i in range(1, n):
        #     for j in range(w + 1):
        #         if 0 <= j - nums[i] <= w:
        #             dp[i][j] = dp[i - 1][j - nums[i]]
        #         if 0 <= j + nums[i] <= w:
        #             dp[i][j] += dp[i - 1][j + nums[i]]
        # return dp[n - 1][target + offset]

        pass


if __name__ == '__main__':
    nums1 = [1, 1, 1, 1, 1]
    target1 = 3
    nums2 = [1]
    target2 = 1

    s = Solution()
    r1 = s.findTargetSumWays(nums1, target1)
    r2 = s.findTargetSumWays(nums2, target2)
    print(r1)
    print(r2)
