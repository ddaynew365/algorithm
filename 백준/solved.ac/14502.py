import sys
from itertools import combinations
from collections import deque
n, m = map(int, sys.stdin.readline().strip().split(" "))
graph = []
for _ in range(n):
  graph.append(list(map(int, sys.stdin.readline().strip().split(" "))))
  
zero_locate = []
virus_locate = []
for y in range(n):
  for x in range(m):
    if graph[y][x] == 0:
      zero_locate.append([y,x])
    elif graph[y][x] == 2:
      virus_locate.append([y,x])

candidates = combinations(zero_locate, 3)

def bfs(graph):
  queue = deque(virus_locate)
  dy = [0, 1,0,-1]
  dx = [1,0,-1,0]
  while queue:
    cy, cx = queue.popleft()
    for i in range(4):
      ny, nx = cy + dy[i], cx +dx[i]
      if 0<= ny < n and 0 <= nx < m and graph[ny][nx] == 0:
        graph[ny][nx] = 2
        queue.append([ny,nx])
  count = 0
  for y in range(n):
    for x in range(m):
      if graph[y][x] == 0:
        count += 1
  return count
    
  
safe_zone = 0
for candidate in candidates:
  g = [[graph[y][x] for x in range(m)] for y in range(n)]
  for y,x in candidate:
    g[y][x] = 1
  if bfs(g) > safe_zone:
    safe_zone = bfs(g)
print(safe_zone)