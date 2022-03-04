# 54. 螺旋矩阵
#
# 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
#
# 示例1：
# 输入：matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# 输出：[1, 2, 3, 6, 9, 8, 7, 4, 5]
#
# 示例2：
# 输入：matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# 输出：[1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
#
# 提示：
#     m == matrix.length
#     n == matrix[i].length
#     1 <= m, n <= 10
#     -100 <= matrix[i][j] <= 100

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # m, n = len(matrix), len(matrix[0])
        # result = []
        # left, right = 0, n - 1
        # top, bottom = 0, m - 1
        # while left <= right and top <= bottom:
        #     for i in range(left, right+1):
        #         result.append(matrix[top][i])
        #     for i in range(top+1, bottom+1):
        #         result.append(matrix[i][right])
        #     if top != bottom:
        #         for i in range(right-1, left-1, -1):
        #             result.append(matrix[bottom][i])
        #     if left != right:
        #         for i in range(bottom-1, top, -1):
        #             result.append(matrix[i][left])
        #
        #     left += 1
        #     right -= 1
        #     top += 1
        #     bottom -= 1
        # return result

        pass


if __name__ == '__main__':
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix3 = [[1, 2, 3]]
    matrix2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    matrix4 = [[1], [5], [9]]

    s = Solution()
    r1 = s.spiralOrder(matrix1)
    r2 = s.spiralOrder(matrix2)
    r3 = s.spiralOrder(matrix3)
    r4 = s.spiralOrder(matrix4)
    print(r1)
    print(r2)
    print(r3)
    print(r4)
