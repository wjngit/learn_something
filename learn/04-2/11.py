# 面试题 17.14. 最小K个数
#
# 设计一个算法，找出数组中最小的k个数。以任意顺序返回这k个数均可。
#
# 示例：
# 输入： arr = [1,3,5,7,2,4,6,8], k = 4
# 输出： [1,2,3,4]
# 提示：
#     0 <= len(arr) <= 100000
#     0 <= k <= min(100000, len(arr))


from typing import List


class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        #     n = len(arr)
        #     if k > n or k == 0:
        #         return []
        #     self.quick_sort(arr, 0, n - 1, k)
        #     return [arr[i] for i in range(k)]
        #
        # def quick_sort(self, data, start, end, k):
        #     m = self.partition(data, start, end)
        #     if m == k - 1:
        #         return
        #     if m > k - 1:
        #         self.quick_sort(data, start, m - 1, k)
        #     else:
        #         self.quick_sort(data, m + 1, end, k)
        #
        # def partition(self, data, start, end):
        #     i, j = start, end - 1
        #     pivot = data[end]
        #     while i < j:
        #         if data[i] < pivot:
        #             i += 1
        #             continue
        #         if data[j] > pivot:
        #             j -= 1
        #             continue
        #         self.swap(data, i, j)
        #         i += 1
        #         j -= 1
        #     if data[j] < pivot:
        #         j += 1
        #     self.swap(data, j, end)
        #     return j
        #
        # def swap(self, data, i, j):
        #     temp = data[i]
        #     data[i], data[j] = data[j], temp

        pass


if __name__ == '__main__':
    arr1 = [1, 3, 5, 7, 2, 4, 6, 8]
    k1 = 4

    s = Solution()
    r1 = s.smallestK(arr1, k1)
    print(r1)
