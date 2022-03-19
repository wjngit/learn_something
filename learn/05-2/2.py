# 15. 三数之和
#
# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。
# 注意：答案中不可以包含重复的三元组。
#
# 示例 1：
# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]
#
# 示例 2：
# 输入：nums = []
# 输出：[]
#
# 示例 3：
# 输入：nums = [0]
# 输出：[]
#
# 提示：
#     0 <= nums.length <= 3000
#     -10^5 <= nums[i] <= 10^5


from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nums.sort()
        # n = len(nums)
        #
        # target_dict = {}
        # for i in range(n):
        #     target_dict[nums[i]] = i
        #
        # result = []
        # for i in range(n):
        #     if i != 0 and nums[i] == nums[i - 1]:
        #         continue
        #
        #     for j in range(i + 1, n):
        #         if j != i + 1 and nums[j] == nums[j - 1]:
        #             continue
        #
        #         target = -1 * (nums[i] + nums[j])
        #         if target not in target_dict:
        #             continue
        #
        #         k = target_dict[target]
        #         if k <= j:
        #             continue
        #         result.append([nums[i], nums[j], nums[k]])
        # return result

        pass


if __name__ == '__main__':
    nums1 = [-1, 0, 1, 2, -1, -4]
    nums2 = []
    nums3 = [1]

    s = Solution()
    r1 = s.threeSum(nums1)
    r2 = s.threeSum(nums2)
    r3 = s.threeSum(nums3)
    print(r1)
    print(r2)
    print(r3)
