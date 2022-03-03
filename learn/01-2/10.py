# 240. 搜索二维矩阵 II
#
# 编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：
# 每行的元素从左到右升序排列。
# 每列的元素从上到下升序排列。
#
# 示例1：
# 输入：
#     matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24],
#              [18, 21, 23, 26, 30]]
#     target = 5
# 输出：true
#
# 示例2：
# 输入：
#     matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24],
#              [18, 21, 23, 26, 30]]
#     target = 20
# 输出：false
#
# 提示：
#     m == matrix.length
#     n == matrix[i].length
#     1 <= n, m <= 300
#     -109 <= matrix[i][j] <= 109
#     每行的所有元素从左到右升序排列
#     每列的所有元素从上到下升序排列
#     -109 <= target <= 109

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # for data in matrix:
        #     left, right = 0, len(data) - 1
        #     while left <= right:
        #         mid = left + (right - left) // 2
        #         if data[mid] > target:
        #             right = mid - 1
        #         elif data[mid] < target:
        #             left = mid + 1
        #         else:
        #             if mid == 0 or data[mid - 1] != target:
        #                 return True
        #             right = mid - 1
        # return False

        pass

        


if __name__ == '__main__':
    matrix1 = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]]
    target1 = 5
    matrix2 = [[
        1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]]
    target2 = 20

    s = Solution()
    r1 = s.searchMatrix(matrix1, target1)
    r2 = s.searchMatrix(matrix2, target2)
    print(r1)
    print(r2)
