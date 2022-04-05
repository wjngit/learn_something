# 213. 打家劫舍 II
#
# 你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。
# 这个地方所有的房屋都 围成一圈 ，这意味着第一个房屋和最后一个房屋是紧挨着的。
# 同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。
# 给定一个代表每个房屋存放金额的非负整数数组，计算你 在不触动警报装置的情况下 ，今晚能够偷窃到的最高金额。
#
# 示例 1：
# 输入：nums = [2,3,2]
# 输出：3
# 解释：你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
#
# 示例 2：
# 输入：nums = [1,2,3,1]
# 输出：4
# 解释：你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
#      偷窃到的最高金额 = 1 + 3 = 4 。
#
# 示例 3：
# 输入：nums = [1,2,3]
# 输出：3
#
# 提示：
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 1000


from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        #     n = len(nums)
        #     if n == 1:
        #         return nums[0]
        #     if n == 2:
        #         return max(nums[0], nums[1])
        #     # 第一个不偷
        #     max1 = self.rob_dp(nums, 1, n - 1)
        #     # 第一个偷
        #     max2 = self.rob_dp(nums, 2, n - 2) + nums[0]
        #     return max(max1, max2)
        #
        # def rob_dp(self, nums, p, r):
        #     n = len(nums)
        #     dp = [[0, 0] for _ in range(n)]
        #     dp[p][0] = 0
        #     dp[p][1] = nums[p]
        #     for i in range(p + 1, r + 1):
        #         dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
        #         dp[i][1] = dp[i - 1][0] + nums[i]
        #     return max(dp[r][0], dp[r][1])

        pass


if __name__ == '__main__':
    nums1 = [2, 3, 2]
    nums2 = [1, 2, 3, 1]
    nums3 = [1, 2, 3]

    s = Solution()
    r1 = s.rob(nums1)
    r2 = s.rob(nums2)
    r3 = s.rob(nums3)
    print(r1)
    print(r2)
    print(r3)
