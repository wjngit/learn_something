# 0-1背包，有n个物品，每个物品只有一个，在不超过背包总重容量前提下，背包装满有多少种装法

def knapsack14(weight: list, n: int, w: int):
    # dp二维数组（0表示没有这种装法）
    dp = [[0] * (w + 1) for _ in range(n)]
    # 初始化第一行
    dp[0][0] = 1
    if weight[0] <= w:
        dp[0][weight[0]] = 1
    for i in range(1, n):
        for j in range(w + 1):
            if j - weight[i] < 0:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - weight[i]]
    # 背包不能装满
    if dp[n - 1][w] == 0:
        return -1
    return dp[n - 1][w]


if __name__ == '__main__':
    weight = [2, 2, 4, 6, 3]
    w = 9
    n = 5
    result = knapsack14(weight, n, w)
    print(result)
