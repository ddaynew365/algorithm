from collections import deque
N = int(input())
grid =[]

for _ in range(N):
  grid.append(list(map(int,input().split())))

dy, dx = [0,0,1,-1],[1,-1,0,0]
def bfs(graph,n):
  queue = deque()
  queue.append((0,0))
  val = graph[0][0]
  visit = [[0 for _ in range(n)] for _ in range(n)]
  visit[0][0] = 1
  while queue:
    y, x = queue.popleft()
    for i in range(4):
      ny, nx = y + dy[i], x + dx[i]
      if 0<=ny<n and 0<=nx <n:
        if graph[ny][nx] != graph[y][x]:
          return 2
        if visit[ny][nx] == 0 :
          queue.append((ny,nx))
          visit[ny][nx] = 1
  return val

count = [0,0]
queue = deque()
queue.append((grid,N))
while queue:
  graph, n = queue.popleft()
  result= bfs(graph, n)
  if result == 2:
    queue.append(([row[:n//2] for row in graph[:n//2]], n//2))
    queue.append(([row[n//2:] for row in graph[:n//2]], n//2))
    queue.append(([row[:n//2] for row in graph[n//2:]], n//2))
    queue.append(([row[n//2:] for row in graph[n//2:]], n//2))
  elif result == 1:
    count[1] += 1
  else:
    count[0] += 1

print(count[0])
print(count[1])
    
    
    