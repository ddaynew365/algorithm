import sys
from collections import deque
m,n = map(int, sys.stdin.readline().strip().split(" "))
graph = []
for _ in range(n):
  graph.append(list(map(int, sys.stdin.readline().strip().split(" "))))
  
queue = deque()
for y in range(n):
  for x in range(m):
    if graph[y][x] == 1:
      queue.append([y,x])
dy, dx = [0,1,0,-1], [1,0,-1,0]
if not queue:
  print(-1)
else:
  while queue:
    cy, cx = queue.popleft()
    for i in range(4):
      ny, nx = cy + dy[i], cx +dx[i]
      if 0 <= ny < n and 0<= nx < m and graph[ny][nx] == 0:
        graph[ny][nx] = graph[cy][cx] + 1
        queue.append([ny, nx])

  is_pass = True
  answer = 0
  for y in range(n):
    for x in range(m):
      if graph[y][x] == 0:
        is_pass = False
        break
      if answer < graph[y][x]:
         answer = graph[y][x]
    if not is_pass:
      break
  if is_pass:
    print(answer-1)
  else:
    print(-1)
        
        