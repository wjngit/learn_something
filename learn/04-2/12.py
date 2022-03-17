# 剑指 Offer 51. 数组中的逆序对
#
# 在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。
#
# 示例 1:
# 输入: [7,5,6,4]
# 输出: 5
#
# 限制：0 <= 数组长度 <= 50000


from typing import List


class Solution:
    count = 0

    def reversePairs(self, nums: List[int]) -> int:
        #     self.merge_sort(nums, 0, len(nums) - 1)
        #     return self.count
        #
        # def merge_sort(self, data, start, end):
        #     if start >= end:
        #         return
        #     mid = start + (end - start) // 2
        #     self.merge_sort(data, start, mid)
        #     self.merge_sort(data, mid + 1, end)
        #     self.merge_func(data, start, mid, end)
        #
        # def merge_func(self, data, start, mid, end):
        #     i, j = start, mid + 1
        #     temp = []
        #     while i <= mid and j <= end:
        #         if data[i] <= data[j]:
        #             temp.append(data[i])
        #             i += 1
        #         else:
        #             self.count += mid + 1 - i
        #             temp.append(data[j])
        #             j += 1
        #     while i <= mid:
        #         temp.append(data[i])
        #         i += 1
        #     while j <= end:
        #         temp.append(data[j])
        #         j += 1
        #     data[start:end + 1] = temp

        pass


if __name__ == '__main__':
    data1 = [7, 5, 6, 4]

    s = Solution()
    r1 = s.reversePairs(data1)
    print(r1)
