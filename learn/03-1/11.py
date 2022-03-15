# 739. 每日温度
#
# 给定一个整数数组 temperatures ，表示每天的温度，返回一个数组 answer ，
# 其中 answer[i] 是指在第 i 天之后，才会有更高的温度。如果气温在这之后都不会升高，请在该位置用 0 来代替。
#
# 示例 1:
# 输入: temperatures = [73,74,75,71,69,72,76,73]
# 输出: [1,1,4,2,1,1,0,0]
#
# 示例 2:
# 输入: temperatures = [30,40,50,60]
# 输出: [1,1,1,0]
#
# 示例 3:
# 输入: temperatures = [30,60,90]
# 输出: [1,1,0]
#
# 提示：
#     1 <= temperatures.length <= 105
#     30 <= temperatures[i] <= 100

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # result = []
        # n = len(temperatures)
        # for i in range(n):
        #     target = temperatures[i]
        #     count = 1
        #     for j in range(i + 1, n):
        #         data = temperatures[j]
        #         if data > target:
        #             result.append(count)
        #             break
        #         count += 1
        #     if count == n - i:
        #         result.append(0)
        # return result

        pass

        # result = []
        # n = len(temperatures)
        # for i in range(n):
        #     target = temperatures[i]
        #     flag = True
        #     for j in range(i + 1, n):
        #         data = temperatures[j]
        #         if data > target:
        #             result.append(j - i)
        #             flag = False
        #             break
        #     if flag:
        #         result.append(0)
        # return result

        pass

        # n = len(temperatures)
        # result = [0] * n
        # stack = []
        # for i in range(n):
        #     while stack and temperatures[stack[-1]] < temperatures[i]:
        #         idx = stack[-1]
        #         result[idx] = i - idx
        #         stack.pop()
        #     stack.append(i)
        # return result

        pass


if __name__ == '__main__':
    temperatures1 = [73, 74, 75, 71, 69, 72, 76, 73]
    temperatures2 = [30, 40, 50, 60]
    temperatures3 = [30, 60, 90]

    s = Solution()
    r1 = s.dailyTemperatures(temperatures1)
    r2 = s.dailyTemperatures(temperatures2)
    r3 = s.dailyTemperatures(temperatures3)
    print(r1)
    print(r2)
    print(r3)
