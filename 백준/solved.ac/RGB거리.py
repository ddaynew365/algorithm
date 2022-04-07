import sys
input = sys.stdin.readline
n = int(input())
house = [[0,0,0]]
for _ in range(n):
  house.append(list(map(int, input().split())))
dp = [[0] * 3 for _ in range(n+1)]
dp[1] = house[1]
for i in range(2,n+1):
  dp[i][0] = house[i][0] + min(dp[i-1][1], dp[i-1][2])
  dp[i][1] = house[i][1] + min(dp[i-1][0], dp[i-1][2])
  dp[i][2] = house[i][2] + min(dp[i-1][0], dp[i-1][1])
answer = min(dp[n])
print(answer)

