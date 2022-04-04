# 完全背包，有n个物品，每个物品有无限个，在不超过背包总重容量前提下，背包可装物品最大值

def knapsack21(weight: list, n: int, w: int):
    # dp二维数组（一个物品怎么装入背包，装0个，1个……k个）
    dp = [[False] * (w + 1) for _ in range(n)]
    # 初始化第一行（背包剩余重量//物品重量）
    for i in range(w // weight[0] + 1):
        dp[0][i] = True
    for i in range(1, n):
        for j in range(w + 1):  # 背包重量
            for c in range(j // weight[i] + 1):
                if dp[i - 1][j - c * weight[i]] is True:
                    dp[i][j] = True
                    # break
    # 从后往前遍历
    for i in range(w, -1, -1):
        if dp[n - 1][i] is True:
            return i
    return 0


if __name__ == '__main__':
    weight = [2, 2, 4, 6, 3]
    w = 9
    n = 5
    result = knapsack21(weight, n, w)
    print(result)
