# 0-1背包，有n个物品，每个物品只有一个，在不超过背包总重容量前提下，背包可装物品最大值

def knapsack11(weight: list, n: int, w: int):
    # dp二维数组（每个阶段决策物品是否装入背包，初始化False表示全不装）
    dp = [[False] * (w + 1) for _ in range(n)]
    # 初始化第一行
    dp[0][0] = True
    if weight[0] <= w:
        dp[0][weight[0]] = True
    for i in range(1, n):
        for j in range(w + 1):
            if dp[i - 1][j] is True or (j - weight[i] >= 0 and dp[i - 1][j - weight[i]] is True):
                dp[i][j] = True
    # 从后往前遍历
    for i in range(w, -1, -1):
        if dp[n - 1][i] is True:
            return i
    return 0


if __name__ == '__main__':
    weight = [2, 2, 4, 6, 3]
    w = 9
    n = 5
    result = knapsack11(weight, n, w)
    print(result)
