import sys
from collections import deque
input = sys.stdin.readline



n, m = map(int, input().split())
dy, dx = [0,0,1,-1], [1,-1,0,0]
grid = list()
for _ in range(n):
  grid.append(list(map(int, input().split())))

bing = deque()
for y in range(n):
  for x in range(m):
    if grid[y][x] != 0:
      bing.append((y,x))
answer = 0

def check(graph):
  is_second = False
  for y in range(n):
    for x in range(m):
      if graph[y][x] != 0:
        if is_second:
          return True
        is_second = True
        queue = deque()
        queue.append((y,x))
        graph[y][x] = 0
        while queue:
          cy, cx = queue.popleft()
          for i in range(4):
            ny, nx = cy + dy[i], cx +dx[i]
            if 0<= ny < n and 0 <= nx < m and graph[ny][nx] !=0:
              graph[ny][nx] = 0
              queue.append((ny,nx))
  return False

while bing:
  answer += 1
  make_zero = False
  dele = []
  for _ in range(len(bing)):
    cy, cx = bing.popleft()
    count = 0
    for i in range(4):
      ny, nx = cy + dy[i], cx + dx[i]
      if 0 <= ny < n and 0 <= nx < m and grid[ny][nx] == 0:
        count += 1
    
    dele.append((cy,cx,count))
  while dele:
    cy, cx, count = dele.pop()
    grid[cy][cx] -= count
    if grid[cy][cx] <= 0:
      grid[cy][cx] = 0
      make_zero = True   
    else:
      bing.append((cy,cx))
      
  if make_zero and check([grid[row][:] for row in range(n)]):
    print(answer)
    answer = -1
    break
if answer != -1:
  print(0)
    