from collections import deque
m, n, h = map(int, input().split())
graph = [[] for  _ in range(h)]
for i in range(h):
  for _ in range(n):
       graph[i].append(list(map(int, input().strip().split())))

queue = deque()
for z in range(h):
  for y in range(n):
    for x in range(m):
      if graph[z][y][x] == 1:
        queue.append([z,y,x])
dz = [0,0,0,0,1,-1]
dy = [-1,0,1,0,0,0]
dx = [0,-1,0,1,0,0]
answer = 0

while queue:
  z,y,x = queue.popleft()
  cur = graph[z][y][x]
  answer = max(cur, answer)
  for i in range(6):
    nz, ny, nx = z +dz[i], y + dy[i], x + dx[i]
    if 0<=ny<n and 0<=nz<h and 0<=nx<m:
      if graph[nz][ny][nx] == 0:
        graph[nz][ny][nx] = cur + 1
        queue.append([nz,ny,nx])  

is_answer = True
for z in range(h):
  for y in range(n):
    for x in range(m):
      if graph[z][y][x] == 0:
        is_answer =False

if is_answer:
  print(answer-1)
else:
  print(-1)

