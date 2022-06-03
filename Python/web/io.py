import sys
input = sys.stdin.readline

n = int(input())
array = [0,0,1,1,1,1,1,1,1,1,1,0]
dp = [0] * 12
for i in range(n - 1):
    for j in range(12):
        dp[j] = array[j]
    for j in range(1, 11):
        array[j] = dp[j - 1] + dp[j + 1]
ans = 0
for k in array:
    ans += k

print(ans)