# 完全背包，有n个物品，每个物品有无限个，在不超过背包总重容量前提下，背包装满有多少种装法

def knapsack24(weight: list, n: int, w: int):
    # dp二维数组（一个物品怎么装入背包，装0个，1个……k个）
    dp = [[0] * (w + 1) for _ in range(n)]
    # 初始化第一行
    for i in range(w // weight[0] + 1):
        dp[0][i * weight[0]] = 1
    for i in range(1, n):
        for j in range(w + 1):
            for c in range(j // weight[i] + 1):
                dp[i][j] += dp[i - 1][j - c * weight[i]]
    # 背包不能装满
    if dp[n - 1][w] == 0:
        return -1
    return dp[n - 1][w]


if __name__ == '__main__':
    weight = [2, 2, 4, 6, 3]
    w = 9
    n = 5
    result = knapsack24(weight, n, w)
    print(result)
