# 48. 旋转图像
#
# 给定一个 n×n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。
# 你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。
#
# 示例1：
# 输入：matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# 输出：[[7, 4, 1], [8, 5, 2], [9, 6, 3]]
#
# 示例2：
# 输入：matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
# 输出：[[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
#
# 提示：
#     n == matrix.length == matrix[i].length
#     1 <= n <= 20
#     -1000 <= matrix[i][j] <= 1000

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # n = len(matrix)
        # temp = [[0] * n for _ in range(n)]
        # for i in range(n):
        #     for j in range(n):
        #         temp[j][n - i - 1] = matrix[i][j]
        # for i in range(n):
        #     for j in range(n):
        #         matrix[i][j] = temp[i][j]

        pass

        # n = len(matrix)
        # for i in range(n // 2):
        #     for j in range(n):
        #         tmp = matrix[i][j]
        #         matrix[i][j] = matrix[n - i - 1][j]
        #         matrix[n - i - 1][j] = tmp
        # for i in range(1, n):
        #     for j in range(i):
        #         tmp = matrix[i][j]
        #         matrix[i][j] = matrix[j][i]
        #         matrix[j][i] = tmp

        pass

        # n = len(matrix)
        # 上下翻转
        # for i in range(n // 2):
        #     for j in range(n):
        #         temp = matrix[i][j]
        #         matrix[i][j] = matrix[n - i - 1][j]
        #         matrix[n - i - 1][j] = temp

        # 左右翻转
        # for i in range(n):
        #     for j in range(i):
        #         temp = matrix[i][j]
        #         matrix[i][j] = matrix[j][i]
        #         matrix[j][i] = temp

        # 主对角线翻转
        # for i in range(n):
        #     for j in range(n // 2):
        #         temp = matrix[i][j]
        #         matrix[i][j] = matrix[i][n - j - 1]
        #         matrix[i][n - j - 1] = temp

        # 副对角线翻转
        # for i in range(n):
        #     for j in range(n - i):
        #         temp = matrix[i][j]
        #         matrix[i][j] = matrix[n - j - 1][n - i - 1]
        #         matrix[n - j - 1][n - i - 1] = temp

        pass

        # n = len(matrix)
        # s1_i, s1_j = 0, 0
        # while n > 1:
        #     s2_i, s2_j = s1_i, s1_j + n - 1
        #     s3_i, s3_j = s1_i + n - 1, s1_j + n - 1
        #     s4_i, s4_j = s1_i + n - 1, s1_j
        #
        #     for move in range(n - 1):
        #         p1_i, p1_j = s1_i, s1_j + move
        #         p2_i, p2_j = s2_i + move, s2_j
        #         p3_i, p3_j = s3_i, s3_j - move
        #         p4_i, p4_j = s4_i - move, s4_j
        #
        #         temp = matrix[p1_i][p1_j]
        #         matrix[p1_i][p1_j] = matrix[p4_i][p4_j]
        #         matrix[p4_i][p4_j] = matrix[p3_i][p3_j]
        #         matrix[p3_i][p3_j] = matrix[p2_i][p2_j]
        #         matrix[p2_i][p2_j] = temp
        #
        #     s1_i += 1
        #     s1_j += 1
        #     n -= 2

        pass


if __name__ == '__main__':
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix2 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]

    s = Solution()
    s.rotate(matrix1)
    s.rotate(matrix2)
    print(matrix1)
    print(matrix2)
    # [[7, 8, 9], [4, 5, 6], [1, 2, 3]]
    # [[3, 2, 1], [6, 5, 4], [9, 8, 7]]
    # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    # [[9, 6, 3], [8, 5, 2], [7, 4, 1]]
