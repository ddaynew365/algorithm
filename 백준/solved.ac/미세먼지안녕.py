R, C, T = map(int, input().split())
grid = []
for _ in range(R):
  grid.append(list(map(int, input().split())))

# 미세먼지
dy, dx = [0,0,1,-1], [1,-1,0,0]

def dust():
  global R, C
  new_graph = [[0] * C for _ in range(R)]
  for y in range(R):
    for x in range(C):  
      if grid[y][x] != 0 and grid[y][x] != -1:
        count = 0
        for i in range(4):
          ny, nx = y+ dy[i], x + dx[i]
          if 0 <= ny < R and 0<=nx <C and grid[ny][nx] != -1:
            count += 1
            new_graph[ny][nx] += grid[y][x] // 5
        new_graph[y][x] -= count * (grid[y][x]//5)
  for y in range(R):
    for x in range(C):
      grid[y][x] += new_graph[y][x]
# 공기 청정기
def clean(locate):
  global R, C
  up, down = locate
  uy, ux = up
  for y in range(uy-1,-1,-1):
    grid[y][0] = grid[y-1][0]
  for x in range(C-1):
    grid[0][x] = grid[0][x+1]
  for y in range(uy):
    grid[y][C-1] = grid[y+1][C-1]
  for x in range(C-1,1,-1):
    grid[uy][x] = grid[uy][x-1]
    
  grid[uy][ux+1] = 0
  doy, dox = down
  
  for y in range(doy+1,R-1):
    grid[y][0] = grid[y+1][0]
  for x in range(C-1):
    grid[R-1][x] = grid[R-1][x+1]
  for y in range(R-1,doy,-1):
    grid[y][C-1] = grid[y-1][C-1]
  for x in range(C-1,1,-1):
    grid[doy][x] = grid[doy][x-1]
  grid[doy][dox+1] = 0
  
cleaner = []
for y in range(R):
  if grid[y][0] == -1:
    cleaner.append((y,0))
for _ in range(T):
  dust()
  clean(cleaner)
answer = 0
for y in range(R):
  for x in range(C):
    answer += grid[y][x]
print(answer+2)
