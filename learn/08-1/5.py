# 78. 子集
#
# 给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
# 解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
#
# 示例 1：
# 输入：nums = [1,2,3]
# 输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
#
# 示例 2：
# 输入：nums = [0]
# 输出：[[],[0]]
#
# 提示：
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# nums 中的所有元素 互不相同


from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #     self.backtrack(nums, 0, [])
        #     return self.result
        #
        # def __init__(self):
        #     self.result = []
        #
        # def backtrack(self, nums, k, path):
        #     if k == len(nums):
        #         self.result.append(path[:])
        #         return
        #     self.backtrack(nums, k + 1, path)
        #     path.append(nums[k])
        #     self.backtrack(nums, k + 1, path)
        #     path.pop()

        pass


if __name__ == '__main__':
    nums1 = [1, 2, 3]
    nums2 = [0]

    s1 = Solution()
    s2 = Solution()
    r1 = s1.subsets(nums1)
    r2 = s2.subsets(nums2)
    print(r1)
    print(r2)
