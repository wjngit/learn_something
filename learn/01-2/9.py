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
        pass


if __name__ == '__main__':
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

    s = Solution()
    r1 = s.spiralOrder(matrix1)
    r2 = s.spiralOrder(matrix2)
    print(r1)
    print(r2)
