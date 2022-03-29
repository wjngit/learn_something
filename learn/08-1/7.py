# 46. 全排列
#
# 给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
#
# 示例 1：
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#
# 示例 2：
# 输入：nums = [0,1]
# 输出：[[0,1],[1,0]]
#
# 示例 3：
# 输入：nums = [1]
# 输出：[[1]]
#
# 提示：
#     1 <= nums.length <= 6
#     -10 <= nums[i] <= 10
#     nums 中的所有整数 互不相同


from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
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
        #     for i in range(len(nums)):
        #         if nums[i] in path:
        #             continue
        #         path.append(nums[i])
        #         self.backtrack(nums, k + 1, path)
        #         path.pop()

        pass


if __name__ == '__main__':
    nums1 = [1, 2, 3]
    nums2 = [0, 1]
    nums3 = [1]

    s1 = Solution()
    s2 = Solution()
    s3 = Solution()
    r1 = s1.permute(nums1)
    r2 = s2.permute(nums2)
    r3 = s3.permute(nums3)
    print(r1)
    print(r2)
    print(r3)
