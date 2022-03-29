# 93. 复原 IP 地址
#
# 有效 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。
# 例如："0.1.2.201" 和 "192.168.1.1" 是 有效 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 和 "192.168@1.1" 是 无效 IP 地址。
# 给定一个只包含数字的字符串 s ，用以表示一个 IP 地址，返回所有可能的有效 IP 地址，这些地址可以通过在 s 中插入 '.' 来形成。
# 你 不能 重新排序或删除 s 中的任何数字。你可以按 任何 顺序返回答案。
#
# 示例 1：
# 输入：s = "25525511135"
# 输出：["255.255.11.135","255.255.111.35"]
#
# 示例 2：
# 输入：s = "0000"
# 输出：["0.0.0.0"]
#
# 示例 3：
# 输入：s = "101023"
# 输出：["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
#
# 提示：
# 1 <= s.length <= 20
# s 仅由数字组成


from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        #     self.backtrack(s, 0, 0, [])
        #     return self.result
        #
        # def __init__(self):
        #     self.result = []
        #
        # def backtrack(self, s, k, step, path):
        #     if step == 4 and k == len(s):
        #         sb = [str(item) for item in path]
        #         self.result.append(".".join(sb))
        #         return
        #     if step > 4:
        #         return
        #     if k == len(s):
        #         return
        #     val = 0
        #     if k < len(s):
        #         val = val * 10 + int(s[k])
        #         path.append(val)
        #         self.backtrack(s, k + 1, step + 1, path)
        #         path.pop()
        #     if s[k] == "0":
        #         return
        #     if k + 1 < len(s):
        #         val = val * 10 + int(s[k + 1])
        #         path.append(val)
        #         self.backtrack(s, k + 2, step + 1, path)
        #         path.pop()
        #     if k + 2 < len(s):
        #         val = val * 10 + int(s[k + 2])
        #         if val <= 255:
        #             path.append(val)
        #             self.backtrack(s, k + 3, step + 1, path)
        #             path.pop()

        pass


if __name__ == '__main__':
    s1s = "25525511135"
    s2s = "0000"
    s3s = "101023"

    s1 = Solution()
    s2 = Solution()
    s3 = Solution()
    r1 = s1.restoreIpAddresses(s1s)
    r2 = s2.restoreIpAddresses(s2s)
    r3 = s3.restoreIpAddresses(s3s)
    print(r1)
    print(r2)
    print(r3)
