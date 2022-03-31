import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
graph = []
for _ in range(n):
  graph.append(list(input().strip()))

dy = [0, 1,-1, 0]
dx = [1, 0 ,0, -1]

def bfs(graph, start, visit):
  queue = deque([start])
  while queue:
    cy, cx = queue.popleft()
    color = graph[cy][cx]
    for i in range(4):
      ny, nx = cy + dy[i], cx + dx[i]
      if 0<=ny<n and 0<=nx<n and graph[ny][nx] == color and visit[ny][nx] == False:
        queue.append([ny, nx])
        visit[ny][nx] = True
  return 1
      

g_count = 0
visit = [[False for _ in range(n)] for _ in range(n)]
for i in range(n):
  for j in range(n):
    if visit[i][j] == False:
      visit[i][j] = True
      g_count += bfs(graph, [i,j], visit)
      
for i in range(n):
  for j in range(n):
     if graph[i][j] == "G":
       graph[i][j] = 'R'


count = 0
visit = [[False for _ in range(n)] for _ in range(n)]
for i in range(n):
  for j in range(n):
    if visit[i][j] == False:
      visit[i][j] = True
      count += bfs(graph, [i,j], visit)
print(g_count, count)
