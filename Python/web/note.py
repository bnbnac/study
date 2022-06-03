n = int(input())

dp = [0, 1]
for i in range(n):
    dp[0] += dp[1]
    dp[1] = dp[0] - dp[1]
print(dp[0] + dp[1])
