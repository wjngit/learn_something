# 42. 接雨水
#
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
#
# 示例 1：
# 输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出：6
# 解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。
#
# 示例 2：
# 输入：height = [4,2,0,3,2,5]
# 输出：9
#
# 提示：
#     n == height.length
#     1 <= n <= 2 * 104
#     0 <= height[i] <= 105


from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # n = len(height)
        # result = 0
        # for i in range(1, n - 1):
        #     left_h = 0
        #     for j in range(i):
        #         if height[j] > left_h:
        #             left_h = height[j]
        #     right_h = 0
        #     for k in range(i + 1, n):
        #         if height[k] > right_h:
        #             right_h = height[k]
        #     carry = min(left_h, right_h) - height[i]
        #     if carry > 0:
        #         result += carry
        # return result

        pass

        # n = len(height)
        # left_h = [0] * n
        # left_max = 0
        # for i in range(n):
        #     left_h[i] = max(left_max, height[i])
        #     left_max = left_h[i]
        #
        # right_h = [0] * n
        # right_max = 0
        # for j in range(n - 1, -1, -1):
        #     right_h[j] = max(right_max, height[j])
        #     right_max = right_h[j]
        #
        # result = 0
        # for k in range(n):
        #     result += min(left_h[k], right_h[k]) - height[k]
        #
        # return result

        pass


if __name__ == '__main__':
    height1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    height2 = [4, 2, 0, 3, 2, 5]

    s = Solution()
    r1 = s.trap(height1)
    r2 = s.trap(height2)
    print(r1)
    print(r2)
