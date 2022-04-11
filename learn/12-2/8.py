# 剑指 Offer 56 - II. 数组中数字出现的次数 II
#
# 在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。
#
# 示例 1：
# 输入：nums = [3,4,3,3]
# 输出：4
#
# 示例 2：
# 输入：nums = [9,1,7,9,7,9,7]
# 输出：1
#
# 限制：
# 1 <= nums.length <= 10000
# 1 <= nums[i] < 2^31


from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        bits = [0] * 32
        mask = 1
        for i in range(32):
            for j in range(n):
                if (nums[j] & mask) != 0:
                    bits[i] = (bits[i] + 1) % 3
            mask <<= 1
        result = 0
        mask = 1
        for i in range(32):
            if bits[i] == 1:
                result += mask
            mask <<= 1
        return result


if __name__ == '__main__':
    nums1 = [3, 4, 3, 3]
    nums2 = [9, 1, 7, 9, 7, 9, 7]

    s = Solution()
    r1 = s.singleNumber(nums1)
    r2 = s.singleNumber(nums2)
    print(r1)
    print(r2)
