# 74. 搜索二维矩阵
#
# 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
#     每行中的整数从左到右按升序排列。
#     每行的第一个整数大于前一行的最后一个整数。
#
# 示例 1：
# 输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# 输出：true
#
# 示例 2：
# 输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# 输出：false
#
# 提示：
#     m == matrix.length
#     n == matrix[i].length
#     1 <= m, n <= 100
#     -10^4 <= matrix[i][j], target <= 10^4


from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # m, n = len(matrix), len(matrix[0])
        # i, j = 0, n - 1
        # while i < m and j >= 0:
        #     if matrix[i][j] == target:
        #         return True
        #     if matrix[i][j] > target:
        #         j -= 1
        #         continue
        #     if matrix[i][j] < target:
        #         i += 1
        #         continue
        #     i += 1
        #     j -= 1
        # return False

        pass

        # m, n = len(matrix), len(matrix[0])
        # low, high = 0, m * n - 1
        # while low <= high:
        #     mid = low + (high - low) // 2
        #     # mid = i * n + j
        #     data = matrix[mid // n][mid % n]
        #     if data == target:
        #         return True
        #     if data > target:
        #         high = mid - 1
        #     else:
        #         low = mid + 1
        # return False

        pass


if __name__ == '__main__':
    matrix1 = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target1 = 3
    matrix2 = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target2 = 13

    s = Solution()
    r1 = s.searchMatrix(matrix1, target1)
    r2 = s.searchMatrix(matrix2, target2)
    print(r1)
    print(r2)
