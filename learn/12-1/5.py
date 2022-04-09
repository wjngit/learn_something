# 剑指 Offer 57 - II. 和为s的连续正数序列
#
# 输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。
# 序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。
#
# 示例 1：
# 输入：target = 9
# 输出：[[2,3,4],[4,5]]
#
# 示例 2：
# 输入：target = 15
# 输出：[[1,2,3,4,5],[4,5,6],[7,8]]
#
# 限制：1 <= target <= 10^5


from typing import List


class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        result = []
        p, q = 1, 2
        total = 3
        while p < q:
            arr = [0] * (q - p + 1)
            if total == target:
                for i in range(p, q + 1):
                    arr[i - p] = i
                result.append(arr)
                total -= p
                p += 1
                q += 1
                total += q
            elif total > target:
                total -= p
                p += 1
            else:
                q += 1
                total += q
        return result


if __name__ == '__main__':
    target1 = 9
    target2 = 15

    s = Solution()
    r1 = s.findContinuousSequence(target1)
    r2 = s.findContinuousSequence(target2)
    print(r1)
    print(r2)
