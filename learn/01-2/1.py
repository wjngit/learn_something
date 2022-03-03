# 面试题 01.08.零矩阵
#
# 编写一种算法，若M × N矩阵中某个元素为0，则将其所在的行与列清零。
#
# 示例1：
# 输入：
# [
#     [1, 1, 1],
#     [1, 0, 1],
#     [1, 1, 1]
# ]
# 输出：
# [
#     [1, 0, 1],
#     [0, 0, 0],
#     [1, 0, 1]
# ]
#
# 示例2：
# 输入：
# [
#     [0, 1, 2, 0],
#     [3, 4, 5, 2],
#     [1, 3, 1, 5]
# ]
# 输出：
# [
#     [0, 0, 0, 0],
#     [0, 4, 5, 0],
#     [0, 3, 1, 0]
# ]

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # row_temp = []
        # col_temp = []
        # for row_index, data_list in enumerate(matrix):
        #     for index, data in enumerate(data_list):
        #         if data == 0:
        #             row_temp.append(row_index)
        #             col_temp.append(index)
        # row_temp = list(set(row_temp))
        # col_temp = list(set(col_temp))
        # for i in row_temp:
        #     temp = matrix[i]
        #     for j in range(len(temp)):
        #         temp[j] = 0
        #
        # for m in col_temp:
        #     for data_ in matrix:
        #         data_[m] = 0

        pass


if __name__ == '__main__':
    l1 = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]
    l2 = [
        [0, 1, 2, 0],
        [3, 4, 5, 2],
        [1, 3, 1, 5]
    ]

    s = Solution()
    s.setZeroes(l1)
    s.setZeroes(l2)
    print(l1)
    print(l2)
