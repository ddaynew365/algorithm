n, k = map(int, input().strip().split(" "))
cargo = []
for _ in range(n):
  w, v = map(int, input().strip().split(" "));
  cargo.append((w,v))

dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(n+1):
  for j in range(k+1):
    if i == 0 or j == 0:
      dp[i][j] = 0
    elif cargo[i-1][0] <= j:
      dp[i][j] = max(cargo[i-1][1] + dp[i-1][j-cargo[i-1][0]], dp[i-1][j])
    else:
      dp[i][j] = dp[i-1][j]
print(dp[n][k])
