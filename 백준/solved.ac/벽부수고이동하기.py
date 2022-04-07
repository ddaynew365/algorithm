import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(input())

dy = [0,0,1,-1]
dx = [1,-1,0,0]
visit = [[2 for _ in range(m)] for _ in range(n)]
# 2: 방문 안함 1:벽뚫고옴 0: 방문
visit[0][0] = 0
def bfs(graph):
  queue = deque([(0,0)])
  res = 0
  while queue:
    res += 1
    for _ in range(len(queue)):
      y, x = queue.popleft()
      if y == n-1 and x ==m-1:
        return res
      for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        if 0<=ny<n and 0<=nx<m:
          if graph[ny][nx] == '0' and visit[ny][nx] > visit[y][x]:
            visit[ny][nx] = visit[y][x]
            queue.append((ny,nx))
          elif graph[ny][nx] == '1' and visit[y][x] == 0:
            visit[ny][nx] = 1
            queue.append((ny,nx))
  return -1
  
answer = bfs(graph)
print(answer)