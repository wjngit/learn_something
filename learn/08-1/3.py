# 17. 电话号码的字母组合
#
# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
#
# 示例 1：
# 输入：digits = "23"
# 输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
#
# 示例 2：
# 输入：digits = ""
# 输出：[]
#
# 示例 3：
# 输入：digits = "2"
# 输出：["a","b","c"]
#
# 提示：
# 0 <= digits.length <= 4
# digits[i] 是范围 ['2', '9'] 的一个数字。


from typing import List

mappings = [""] * 10
mappings[2] = "abc"
mappings[3] = "def"
mappings[4] = "ghi"
mappings[5] = "jkl"
mappings[6] = "mno"
mappings[7] = "pqrs"
mappings[8] = "tuv"
mappings[9] = "wxyz"


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #     if len(digits) == 0:
        #         return self.result
        #     path = [None] * len(digits)
        #     self.backtrack(digits, mappings, 0, path)
        #     return self.result
        #
        # def __init__(self):
        #     self.result = []
        #
        # def backtrack(self, digits, mappings, k, path):
        #     if k == len(digits):
        #         self.result.append("".join(path))
        #         return
        #     mapping = mappings[int(digits[k])]
        #     for i in range(len(mapping)):
        #         path[k] = mapping[i]
        #         self.backtrack(digits, mappings, k + 1, path)

        pass


if __name__ == '__main__':
    digits1 = "23"
    digits2 = ""
    digits3 = "2"

    s1 = Solution()
    s2 = Solution()
    s3 = Solution()
    r1 = s1.letterCombinations(digits1)
    r2 = s2.letterCombinations(digits2)
    r3 = s3.letterCombinations(digits3)
    print(r1)
    print(r2)
    print(r3)
