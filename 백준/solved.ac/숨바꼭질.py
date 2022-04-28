N, K = map(int, input().split())
INF = int(1e9)
dp = [INF for _ in range(max(K+2,N+2))]
dp[N] = 0
if 2*N <K+2 and N != 0:
  dp[2*N] = 1
# print(dp)
for i in range(N-1,-1,-1):
  dp[i] =dp[i+1] + 1
  if 2*i < K+2:
    dp[2*i] = min(dp[i] + 1,dp[2*i])
# print(dp)    
for i in range(N+1,K+1):
  dp[i] = min(dp[i-1] +1, dp[i+1] +1, dp[i])
  if 2*i < K+2:
    dp[2*i] = min(dp[i] + 1,dp[2*i])
# print(dp)
print(dp[K])
