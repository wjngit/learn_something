# 40. 组合总和 II
#
# 给定一个候选人编号的集合 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
# candidates 中的每个数字在每个组合中只能使用 一次 。
# 注意：解集不能包含重复的组合。
#
# 示例 1:
# 输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 输出:
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
#
# 示例 2:
# 输入: candidates = [2,5,2,1,2], target = 5,
# 输出:
# [
# [1,2,2],
# [5]
# ]
#
# 提示:
# 1 <= candidates.length <= 100
# 1 <= candidates[i] <= 50
# 1 <= target <= 30


from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        #     count_dict = {}
        #     for num in candidates:
        #         if num in count_dict:
        #             count_dict[num] += 1
        #         else:
        #             count_dict[num] = 1
        #     nums, counts = [], []
        #     for num, count in count_dict.items():
        #         nums.append(num)
        #         counts.append(count)
        #     self.backtrack(nums, counts, 0, target, [])
        #     return self.result
        #
        # def __init__(self):
        #     self.result = []
        #
        # def backtrack(self, nums, counts, k, diff, path):
        #     if diff == 0:
        #         self.result.append(path[:])
        #         return
        #     if k == len(nums) or diff < 0:
        #         return
        #     for count in range(counts[k] + 1):
        #         for _ in range(count):
        #             path.append(nums[k])
        #         self.backtrack(nums, counts, k + 1, diff - nums[k] * count, path)
        #         for _ in range(count):
        #             path.pop()

        pass


if __name__ == '__main__':
    candidates1 = [10, 1, 2, 7, 6, 1, 5]
    target1 = 8
    candidates2 = [2, 5, 2, 1, 2]
    target2 = 5

    s1 = Solution()
    s2 = Solution()
    r1 = s1.combinationSum2(candidates1, target1)
    r2 = s2.combinationSum2(candidates2, target2)
    print(r1)
    print(r2)
