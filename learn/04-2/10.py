# 215. 数组中的第K个最大元素
#
# 给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
# 请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
#
# 示例 1:
# 输入: [3,2,1,5,6,4] 和 k = 2
# 输出: 5
#
# 示例 2:
# 输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
# 输出: 4


from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #     n = len(nums)
        #     if n < k:
        #         return -1
        #     return self.quick_sort(nums, 0, n - 1, k)
        #
        # def quick_sort(self, nums, start, end, k):
        #     if start > end:
        #         return -1
        #     mid = self.partition(nums, start, end)
        #     target = mid - start + 1
        #     if target == k:
        #         return nums[mid]
        #     if target > k:
        #         return self.quick_sort(nums, start, mid - 1, k)
        #     return self.quick_sort(nums, mid + 1, end, k - target)
        #
        # def partition(self, nums, start, end):
        #     i, j = start, end - 1
        #     pivot = nums[end]
        #     while i < j:
        #         if nums[i] >= pivot:
        #             i += 1
        #             continue
        #         if nums[j] < pivot:
        #             j -= 1
        #             continue
        #         self.swap(nums, i, j)
        #         i += 1
        #         j -= 1
        #     if nums[j] >= pivot:
        #         j += 1
        #     else:
        #         if j < start:
        #             j = start
        #     self.swap(nums, j, end)
        #     return j
        #
        # def swap(self, data, i, j):
        #     temp = data[i]
        #     data[i], data[j] = data[j], temp

        pass


if __name__ == '__main__':
    l1 = [3, 2, 1, 5, 6, 4]
    k1 = 2
    l2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k2 = 4
    l3 = [1]
    k3 = 1
    l4 = [2, 1]
    k4 = 1

    s = Solution()
    r4 = s.findKthLargest(l4, k4)
    r3 = s.findKthLargest(l3, k3)
    r1 = s.findKthLargest(l1, k1)
    r2 = s.findKthLargest(l2, k2)
    print(r1)
    print(r2)
    print(r3)
    print(r4)
