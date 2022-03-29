# 77. 组合
#
# 给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。
# 你可以按 任何顺序 返回答案。
#
# 示例 1：
# 输入：n = 4, k = 2
# 输出：
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]
#
# 示例 2：
# 输入：n = 1, k = 1
# 输出：[[1]]
#
# 提示：
# 1 <= n <= 20
# 1 <= k <= n


from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.backtrack(n, k, 1, [])
        return self.result

    def __init__(self):
        self.result = []

    def backtrack(self, n, k, step, path):
        if len(path) == k:
            self.result.append(path[:])
            return
        if step == n + 1:
            return
        self.backtrack(n, k, step + 1, path)
        path.append(step)
        self.backtrack(n, k, step + 1, path)
        path.pop()


if __name__ == '__main__':
    n1 = 4
    k1 = 2
    n2 = 1
    k2 = 1

    s1 = Solution()
    s2 = Solution()
    r1 = s1.combine(n1, k1)
    r2 = s2.combine(n2, k2)
    print(r1)
    print(r2)
