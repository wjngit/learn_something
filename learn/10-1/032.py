# 多重背包，有n个物品，每个物品有 有限 个，在不超过背包总重容量前提下，背包能否装满

def knapsack32(weight: list, count: list, n: int, w: int):
    # dp二维数组（一个物品怎么装入背包，装0个，1个……k个）
    dp = [[False] * (w + 1) for _ in range(n)]
    # 初始化第一行
    for i in range(min(w // weight[0] + 1, count[0] + 1)):
        dp[0][i] = True
    for i in range(1, n):
        for j in range(w + 1):
            for c in range(min(j // weight[i] + 1, count[i] + 1)):
                if dp[i - 1][j - c * weight[i]]:
                    dp[i][j] = True
                    # break
    return dp[n - 1][w]


if __name__ == '__main__':
    weight = [2, 2, 4, 6, 3]
    count = [2, 3, 1, 2, 3]
    w = 9
    n = 5
    result = knapsack32(weight, count, n, w)
    print(result)
