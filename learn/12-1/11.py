# 238. 除自身以外数组的乘积
#
# 给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积 。
# 题目数据 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内。
# 请不要使用除法，且在 O(n) 时间复杂度内完成此题。
#
# 示例 1:
# 输入: nums = [1,2,3,4]
# 输出: [24,12,8,6]
#
# 示例 2:
# 输入: nums = [-1,1,0,-3,3]
# 输出: [0,0,9,0,0]
#
# 提示：
# 2 <= nums.length <= 10^5
# -30 <= nums[i] <= 30
# 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内
#
# 进阶：你可以在 O(1) 的额外空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）


from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # n = len(nums)
        # left_products = [0] * n
        # product = 1
        # for i in range(n):
        #     product *= nums[i]
        #     left_products[i] = product
        #
        # right_products = [0] * n
        # product = 1
        # for i in range(n - 1, -1, -1):
        #     product *= nums[i]
        #     right_products[i] = product
        #
        # result = [None] * n
        # for i in range(n):
        #     result[i] = 1
        #     if i >= 1:
        #         result[i] *= left_products[i - 1]
        #     if i < n - 1:
        #         result[i] *= right_products[i + 1]
        # return result

        pass

        # n = len(nums)
        # result = [None] * n
        # left_product = 1
        # for i in range(n):
        #     result[i] = left_product
        #     left_product *= nums[i]
        # right_product = 1
        # for i in range(n - 1, -1, -1):
        #     result[i] *= right_product
        #     right_product *= nums[i]
        # return result

        pass


if __name__ == '__main__':
    nums1 = [1, 2, 3, 4]
    nums2 = [-1, 1, 0, -3, 3]

    s = Solution()
    r1 = s.productExceptSelf(nums1)
    r2 = s.productExceptSelf(nums2)
    print(r1)
    print(r2)
