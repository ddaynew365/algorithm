import sys
r, c = map(int, sys.stdin.readline().strip().split(" "))
graph = []
for _ in range(r):
  graph.append(list(sys.stdin.readline().strip()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 0
visit = {graph[0][0]}

def dfs(y,x, count):
  global answer
  answer = max(answer, count)
  for i in range(4):
    ny, nx  = y + dy[i], x + dx[i]
    if 0 <= ny < r and 0 <= nx < c and not graph[ny][nx] in visit:
      visit.add(graph[ny][nx])
      dfs(ny,nx, count +1)
      visit.remove(graph[ny][nx])


dfs(0,0, 1)
print(answer)