# 二维费用背包，有n个物品，每个物品只有一个，价值各不相同，在不超过背包总重容量前提下，背包可装物品最大 价值（不是重量）

def knapsack11(weight: list, value: list, n: int, w: int):
    # dp二维数组（每个阶段决策物品是否装入背包之后的价值）
    dp = [[float('-inf')] * (w + 1) for _ in range(n)]
    # 初始化第一行
    dp[0][0] = 0
    if weight[0] <= w:
        dp[0][weight[0]] = value[0]
    for i in range(1, n):
        for j in range(w + 1):
            if dp[i - 1][j] != float('-inf'):
                dp[i][j] = max(dp[i][j], dp[i - 1][j])
            if j - weight[i] >= 0 and dp[i - 1][j - weight[i]] != float('-inf'):
                dp[i][j] = max(dp[i][j], dp[i - 1][j - weight[i]] + value[i])
    res = float('-inf')
    for i in range(w + 1):
        if dp[n - 1][i] > res:
            res = dp[n - 1][i]
    return res


if __name__ == '__main__':
    weight = [2, 2, 4, 6, 3]
    value = [3, 4, 8, 9, 6]
    w = 9
    n = 5
    result = knapsack11(weight, value, n, w)
    print(result)
