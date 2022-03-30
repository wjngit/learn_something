# 216. 组合总和 III
#
# 找出所有相加之和为 n 的 k 个数的组合，且满足下列条件：
# 只使用数字1到9
# 每个数字 最多使用一次
# 返回 所有可能的有效组合的列表 。该列表不能包含相同的组合两次，组合可以以任何顺序返回。
#
# 示例 1:
# 输入: k = 3, n = 7
# 输出: [[1,2,4]]
# 解释: 1 + 2 + 4 = 7 没有其他符合的组合了。
#
# 示例 2:
# 输入: k = 3, n = 9
# 输出: [[1,2,6], [1,3,5], [2,3,4]]
# 解释:
# 1 + 2 + 6 = 9
# 1 + 3 + 5 = 9
# 2 + 3 + 4 = 9
# 没有其他符合的组合了。
#
# 示例 3:
# 输入: k = 4, n = 1
# 输出: []
# 解释: 不存在有效的组合。
# 在[1,9]范围内使用4个不同的数字，我们可以得到的最小和是1+2+3+4 = 10，因为10 > 1，没有有效的组合。
#
# 提示:
# 2 <= k <= 9
# 1 <= n <= 60


from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        #     self.backtrack(k, n, 1, 0, [])
        #     return self.result
        #
        # def __init__(self):
        #     self.result = []
        #
        # def backtrack(self, k, n, step, total, path):
        #     if total == n and len(path) == k:
        #         self.result.append(path[:])
        #         return
        #     # if step > 9:
        #     if total > n or len(path) > k or step > 9:
        #         return
        #     self.backtrack(k, n, step + 1, total, path)
        #     path.append(step)
        #     # if total + step <= n or len(path) <= k:
        #     #     self.backtrack(k, n, step + 1, total + step, path)
        #     self.backtrack(k, n, step + 1, total + step, path)
        #     path.pop()

        pass


if __name__ == '__main__':
    k1 = 3
    n1 = 7
    k2 = 3
    n2 = 9
    k3 = 4
    n3 = 1

    s1 = Solution()
    s2 = Solution()
    s3 = Solution()
    r1 = s1.combinationSum3(k1, n1)
    r2 = s2.combinationSum3(k2, n2)
    r3 = s3.combinationSum3(k3, n3)
    print(r1)
    print(r2)
    print(r3)
