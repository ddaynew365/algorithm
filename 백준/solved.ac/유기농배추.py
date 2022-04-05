from collections import deque
answer = []
t = int(input())
dy, dx = [0,0,1,-1], [1,-1,0,0]

def bfs(graph, y, x):
  queue = deque()
  queue.append([y,x])
  graph[y][x] = 0
  while queue:
    y, x = queue.popleft()
    for i in range(4):
      ny, nx = y + dy[i], x + dx[i]
      if 0 <= ny < n and 0 <= nx < m and graph[ny][nx] == 1:
        graph[ny][nx] = 0
        queue.append([ny, nx])
        
for _ in range(t):
  m, n, k = map(int, input().split())
  graph = [[0 for _ in range(m)] for _ in range(n)]
  for _ in range(k):
    x, y = map(int, input().split())
    graph[y][x] = 1
    
  count = 0
  for y in range(n):
    for x in range(m):
      if graph[y][x] == 1:
        bfs(graph, y , x)
        count += 1
  answer.append(count)

for num in answer:
  print(num)