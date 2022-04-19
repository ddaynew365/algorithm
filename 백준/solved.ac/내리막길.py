import sys
input = sys.stdin.readline
M, N = map(int, input().split())
grid = []
for _ in range(M):
  grid.append(list(map(int, input().split())))
dp_grid = [[-1 for _ in range(N)] for _ in range(M)]
answer = 0
start = (0,0)
target= (M-1, N-1)
visit = [start]
dy, dx = [0,0,1,-1], [1,-1,0,0]

def dfs(cur):
  if cur == target:
    return 1
  cy, cx = cur
  if dp_grid[cy][cx] != -1:
    return dp_grid[cy][cx]
  cur_val = grid[cy][cx]
  dp_grid[cy][cx] = 0
  for i in range(4):
    ny, nx = cy + dy[i], cx+dx[i]
    if 0<= ny < M and 0<= nx < N and grid[ny][nx] < cur_val:
      if (ny,nx) not in visit:
        visit.append((ny,nx))
        dp_grid[cy][cx] += dfs((ny,nx))
        visit.pop()
  return dp_grid[cy][cx]

answer = dfs(start)
print(answer)