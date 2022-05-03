import sys
input = sys.stdin.readline

n = int(input())
answer = 0
g = [0]
dp = [0] * (n+1)
for _ in range(n):
  g.append(int(input()))
  
if n < 3:
  answer = sum(g)
else:
  dp[1] = g[1]
  dp[2] = g[1] + g[2]

for i in range(3,n+1):
  dp[i] = max(dp[i-3]+g[i-1] + g[i], dp[i-2]+g[i],dp[i-1])
  answer = max(answer, dp[i])

print(answer)