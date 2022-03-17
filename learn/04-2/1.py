# 面试题 10.01. 合并排序的数组
#
# 给定两个排序后的数组 A 和 B，其中 A 的末端有足够的缓冲空间容纳 B。 编写一个方法，将 B 合并入 A 并排序。
# 初始化 A 和 B 的元素数量分别为 m 和 n。
#
# 示例:
#     输入:
#     A = [1,2,3,0,0,0], m = 3
#     B = [2,5,6],       n = 3
#     输出: [1,2,2,3,5,6]
#
# 说明:A.length == n + m


from typing import List


class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify A in-place instead.
        """
        # max_index = len(A) - 1
        # i, j = m - 1, n - 1
        # while i >= 0 and j >= 0:
        #     if A[i] >= B[j]:
        #         A[max_index] = A[i]
        #         i -= 1
        #     else:
        #         A[max_index] = B[j]
        #         j -= 1
        #     max_index -= 1
        # while i >= 0:
        #     A[max_index] = A[i]
        #     i -= 1
        #     max_index -= 1
        # while j >= 0:
        #     A[max_index] = B[j]
        #     j -= 1
        #     max_index -= 1

        pass


if __name__ == '__main__':
    A = [1, 2, 3, 0, 0, 0]
    m = 3
    B = [2, 5, 6]
    n = 3
    A1 = [0]
    m1 = 0
    B1 = [2]
    n1 = 1

    s = Solution()
    s.merge(A, m, B, n)
    s.merge(A1, m1, B1, n1)
    print(A)
    print(A1)
