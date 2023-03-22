import sys

si = sys.stdin.readline

dp = [
    [0 for _ in range(15)]
    for _ in range(15)
]
# 초기화
for i in range(15):
    dp[i][0] = 1
    dp[0][i] = i + 1

for i in range(1, 15):
    for j in range(1, 15):
        dp[i][j] = sum(dp[i-1][:j+1])

t = int(si())
for _ in range(t):
    k = int(si())
    n = int(si())
    print(dp[k][n-1])