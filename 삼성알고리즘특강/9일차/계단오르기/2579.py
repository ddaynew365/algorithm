import sys
input = sys.stdin.readline
n = int(input().strip())
starirs = [0]
for _ in range(n):
    starirs.append(int(input().strip()))

dp= [[0 for _ in range(2)] for _ in range(n+1)]
dp[1][0] = starirs[1]
dp[1][1] = starirs[1]
for i in range(2,n+1):
    dp[i][0] = dp[i-1][1] + starirs[i]
    dp[i][1] = max(dp[i - 2][0], dp[i - 2][1]) + starirs[i]

print(max(dp[n]))