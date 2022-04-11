# 剑指 Offer 56 - I. 数组中数字出现的次数
#
# 一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。
# 请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。
#
# 示例 1：
# 输入：nums = [4,1,4,6]
# 输出：[1,6] 或 [6,1]
#
# 示例 2：
# 输入：nums = [1,2,10,4,1,4,3,3]
# 输出：[2,10] 或 [10,2]
#
# 限制：2 <= nums.length <= 10000


from typing import List


class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        xorResult = 0
        n = len(nums)
        for i in range(n):
            xorResult ^= nums[i]
        tag = 1
        while xorResult & tag == 0:
            tag = tag << 1
        a = 0
        b = 0
        for i in range(n):
            if (nums[i] & tag) == 0:
                a ^= nums[i]
            else:
                b ^= nums[i]
        return [a, b]


if __name__ == '__main__':
    nums1 = [4, 1, 4, 6]
    nums2 = [1, 2, 10, 4, 1, 4, 3, 3]

    s = Solution()
    r1 = s.singleNumbers(nums1)
    r2 = s.singleNumbers(nums2)
    print(r1)
    print(r2)
