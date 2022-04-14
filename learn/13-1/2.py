# P为给定的二维平面整数点集。
# 定义 P 中某点x，如果x满足 P 中任意点都不在 x 的右上方区域内（横纵坐标都大于x），则称其为“最大的”。
# 求出所有“最大的”点的集合

def func(data):
    sort_data = sorted(data, key=lambda x: x[0])
    res = []
    for i in range(len(sort_data)):
        target = sort_data[i]
        flag = True
        for j in range(i + 1, len(sort_data)):
            if sort_data[j][1] > target[1]:
                flag = False
                break
        if flag:
            res.append(target)
    return res


if __name__ == '__main__':
    data = [[1, 2], [5, 3], [4, 6], [7, 5], [9, 0]]
    r = func(data)
    print(r)
