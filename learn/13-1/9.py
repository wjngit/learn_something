# n*n的矩阵，只能向右或向下移动，从最左上方移动到最右下方，把所有的路径输出。
res_path = []


def func(matrix, m, n):
    func_r(matrix, 0, 0, m, n, [])
    return res_path


def func_r(matrix, i, j, m, n, path):
    path.append(matrix[i][j])
    if i == m - 1 and j == n - 1:
        res_path.append(path[:])
        path.pop()  # 这里需要回退
        return
    for data in [[1, 0], [0, 1]]:
        ni = data[0] + i
        nj = data[1] + j
        if 0 <= ni < m and 0 <= nj < n:
            func_r(matrix, ni, nj, m, n, path)
    path.pop()  # 这里回退
