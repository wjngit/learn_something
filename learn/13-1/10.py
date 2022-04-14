# Z国的货币系统包含面值1元、4元、16元、64元共计4种硬币，以及面值1024元的纸币。
# 现在小Y使用1024元的纸币购买了一件价值为 0<val<=1024 的商品，请问最少他会收到多少硬币？

def func(coins, val):
    amount = 1024 - val
    n = len(coins)
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for j in range(n):
            if i - coins[j] >= 0 and dp[i - coins[j]] != float("inf") and dp[i - coins[j]] + 1 < dp[i]:
                dp[i] = dp[i - coins[j]] + 1
    if dp[amount] == float("inf"):
        return -1
    return dp[amount]
