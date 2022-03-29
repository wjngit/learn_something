# 22. 括号生成
#
# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
#
# 示例 1：
# 输入：n = 3
# 输出：["((()))","(()())","(())()","()(())","()()()"]
#
# 示例 2：
# 输入：n = 1
# 输出：["()"]
#
# 提示：1 <= n <= 8


from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #     path = [None] * 2 * n
        #     self.backtrack(n, 0, 0, 0, path)
        #     return self.result
        #
        # def __init__(self):
        #     self.result = []
        #
        # def backtrack(self, n, leftUsed, rightUesd, k, path):
        #     if k == 2 * n:
        #         self.result.append("".join(path))
        #         return
        #     if leftUsed > rightUesd:
        #         path[k] = ")"
        #         self.backtrack(n, leftUsed, rightUesd + 1, k + 1, path)
        #     if leftUsed < n:
        #         path[k] = "("
        #         self.backtrack(n, leftUsed + 1, rightUesd, k + 1, path)

        pass


if __name__ == '__main__':
    n1 = 3
    n2 = 1

    s1 = Solution()
    s2 = Solution()
    r1 = s1.generateParenthesis(n1)
    r2 = s2.generateParenthesis(n2)
    print(r1)
    print(r2)
