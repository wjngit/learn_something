# 90. 子集 II
#
# 给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。
# 解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。
#
# 示例 1：
# 输入：nums = [1,2,2]
# 输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]
#
# 示例 2：
# 输入：nums = [0]
# 输出：[[],[0]]
#
# 提示：
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10


from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        hm = {}
        for i in nums:
            if i in hm:
                hm[i] += 1
            else:
                hm[i] = 1
        unique_num, counts = [], []
        for num, count in hm.items():
            unique_num.append(num)
            counts.append(count)
        self.backtrack(unique_num, counts, 0, [])
        return self.result

    def __init__(self):
        self.result = []

    def backtrack(self, unique_num, counts, k, path):
        if k == len(unique_num):
            self.result.append(path[:])
            return
        for count in range(counts[k] + 1):
            for i in range(count):
                path.append(unique_num[k])
            self.backtrack(unique_num, counts, k + 1, path)
            for i in range(count):
                path.pop()


if __name__ == '__main__':
    nums1 = [1, 2, 2]
    nums2 = [0]

    s1 = Solution()
    s2 = Solution()
    r1 = s1.subsetsWithDup(nums1)
    r2 = s2.subsetsWithDup(nums2)
    print(r1)
    print(r2)
