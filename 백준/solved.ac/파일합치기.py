t = int(input())
for _ in range(t):
  n = int(input())
  arr = list(map(int, input().split()))
  lsum = [0]
  for s in arr:
    lsum.append(lsum[-1] + s)
  dp = [[0] * (n+1) for _ in range(n+1)]
  for i in range(2, n+1):
    for j in range(1,n-i+2):
      dp[j][j+i-1] = 1e9
      for k in range(i-1):
        dp[j][j+i-1] = min(dp[j][j+k] +dp[j+k+1][j+i-1]+ lsum[j+i-1] -lsum[j-1], dp[j][j+i-1]) 
  print(dp[1][n])