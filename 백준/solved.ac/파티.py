import sys
from heapq import heappop, heappush
input = sys.stdin.readline
n, m, x = map(int, input().split(" "))
graph = [[] for _ in range(n+1)]
for _ in range(m):
  start, end, cost =map(int,input().split(" "))
  graph[start].append([cost, end])

## 돌아오기
def back():
  dist = [1e9] * (n+1)
  dist[x] = 0
  queue = [[0, x]]
  while queue:
    cost, cur = heappop(queue)
    if dist[cur] < cost:
      continue
    for next_cost, next in graph[cur]:
      ncost = cost + next_cost
      if dist[next] > ncost:
        dist[next] = ncost
        heappush(queue, [ncost,next])
  return dist

def dys(start):
  dist = [1e9] * (n+1)
  queue = [[0,start]]
  while queue:
    cost, cur = heappop(queue)
    if dist[cur] < cost:
      continue
    for next_cost, next in graph[cur]:
      ncost = cost + next_cost
      if ncost< dist[next]:
        dist[next] = ncost
        heappush(queue, [ncost, next])
  return dist[x]

answer = 0
visit = back()
for start in range(1,n+1):
  total = dys(start)
  if start == x:
    continue
  if total > 0:
    total += visit[start]
    answer = max(answer, total)
print(answer)