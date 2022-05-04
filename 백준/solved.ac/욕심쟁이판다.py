import sys
input = sys.stdin.readline
sys.setrecursionlimit(250000)
n = int(input().rstrip())
grid = []
for _ in range(n):
  grid.append(list(map(int, input().split())))

dp = [[-1 for _ in range(n)] for _ in range(n)]
dy, dx = [1,-1,0,0], [0,0,1,-1]
answer = 0

def dfs(y,x):
  global answer
  
  if dp[y][x] != -1:return dp[y][x]
  
  dp[y][x] = 1
  tmp = 0
  
  for i in range(4):
    ny,nx = y+dy[i], x+dx[i]
    if 0<= ny <n and 0<=nx <n and grid[y][x] < grid[ny][nx]:
      dp[y][x] = max(dfs(ny,nx)+1, dp[y][x])

  answer = max(answer,dp[y][x])
  return dp[y][x]


for i in range(n):
  for j in range(n):
    if dp[i][j] == -1:
      dfs(i,j)

print(answer)