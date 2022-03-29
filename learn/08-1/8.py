# 47. 全排列 II
#
# 给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。
#
# 示例 1：
# 输入：nums = [1,1,2]
# 输出：
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
#
# 示例 2：
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#
# 提示：
# 1 <= nums.length <= 8
# -10 <= nums[i] <= 10

from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        #     hm = {}
        #     for i in nums:
        #         if i in hm:
        #             hm[i] += 1
        #         else:
        #             hm[i] = 1
        #     unique_num, counts = [], []
        #     for num, count in hm.items():
        #         unique_num.append(num)
        #         counts.append(count)
        #     self.backtrack(unique_num, counts, 0, [], len(nums))
        #     return self.result
        #
        # def __init__(self):
        #     self.result = []
        #
        # def backtrack(self, unique_nums, counts, k, path, n):
        #     if k == n:
        #         self.result.append(path[:])
        #         return
        #     for i in range(len(unique_nums)):
        #         if counts[i] == 0:
        #             continue
        #         path.append(unique_nums[i])
        #         counts[i] -= 1
        #         self.backtrack(unique_nums, counts, k + 1, path, n)
        #         path.pop()
        #         counts[i] += 1

        pass


if __name__ == '__main__':
    nums1 = [1, 1, 2]
    nums2 = [1, 2, 3]

    s1 = Solution()
    s2 = Solution()
    r1 = s1.permuteUnique(nums1)
    r2 = s2.permuteUnique(nums2)
    print(r1)
    print(r2)
