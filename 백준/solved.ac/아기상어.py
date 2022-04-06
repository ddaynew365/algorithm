from collections import deque
n = int(input())
graph= []
for _ in range(n):
  graph.append(list(map(int, input().split())))
shark = []
slevel = [2,2]
for y in range(n):
  for x in range(n):
    num = graph[y][x]
    if num == 9:
      shark = [y,x]
      graph[y][x] = 0

count = 0
eat = True
while eat:
  queue = deque()
  dy, dx = [-1,0,0,1], [0,-1,1,0]
  y , x = shark
  eat = False
  queue.append([y, x, 0])
  visit = []
  while queue:
    if eat:
      break
    queue = deque(sorted(queue, key=lambda x: (x[0],x[1])))
    for _ in range(len(queue)):
      cy, cx, dist = queue.popleft()
      if 0 < graph[cy][cx] < slevel[1]:
        count = count + dist
        slevel[0] -= 1
        if slevel[0] == 0:
          slevel[1] += 1
          slevel[0] = slevel[1]
        shark = [cy, cx]
        graph[cy][cx] = 0
        eat = True
        break
      for i in range(4):
        ny, nx = cy + dy[i], cx + dx[i]
        if 0<=ny<n and 0<=nx<n:
          if [ny,nx] not in visit and graph[ny][nx] <= slevel[1]:
            queue.append([ny, nx, dist+1])
            visit.append([ny, nx]) 
print(count)
  
  
