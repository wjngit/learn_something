# 0-1背包问题
# 有一个背包，最多装w的重量，有一些物品items（重量不一样），选出装最重的重量是多少
from typing import List


class Solution:
    def solve(self, w: int, items: List[int]) -> int:
        #     self.backtrack(items, 0, 0, w)
        #     return self.max_weight
        #
        # def __init__(self):
        #     self.max_weight = 0
        #
        # def backtrack(self, items, k, cw, w):
        #     # 决策次数到了或已经装满了
        #     if k == len(items) or cw == w:
        #         if cw > self.max_weight:
        #             self.max_weight = cw
        #         return
        #     # 不装的情况
        #     self.backtrack(items, k + 1, cw, w)
        #     if cw + items[k] <= w:
        #         self.backtrack(items, k + 1, cw + items[k], w)

        pass


# 正则表达式
# *代表多个，?代表0个或一个，实现这个正则
class Solution2:
    def solve(self, text: str, pattern: str) -> bool:
        #     self.backtrack(text, pattern, 0, 0)
        #     return self.matched
        #
        # def __init__(self):
        #     self.matched = False
        #
        # def backtrack(self, text, pattern, ti, pj):
        #     if pj == len(pattern):
        #         if ti == len(text):
        #             self.matched = True
        #         return
        #     # 匹配多个
        #     if pattern[pj] == "*":
        #         for k in range(len(text) - ti):
        #             self.backtrack(text, pattern, ti + k, pj + 1)
        #     elif pattern[pj] == "?":
        #         # 匹配0个
        #         self.backtrack(text, pattern, ti, pj + 1)
        #         # 匹配一个
        #         if ti < len(text):
        #             self.backtrack(text, pattern, ti + 1, pj + 1)
        #     # 匹配一个字符
        #     elif ti < len(text) and pattern[pj] == text[ti]:
        #         self.backtrack(text, pattern, ti + 1, pj + 1)

        pass


if __name__ == '__main__':
    items = [3, 4, 5, 6, 7]
    w = 11
    s = Solution()
    r = s.solve(w, items)
    print(r)

    text = "adcabef"
    pattern = "a*b?f"
    s1 = Solution2()
    r1 = s1.solve(text, pattern)
    print(r1)
