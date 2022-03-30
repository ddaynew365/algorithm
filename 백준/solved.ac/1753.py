import heapq, sys
from collections import defaultdict
input = sys.stdin.readline
v_num, e = map(int, input().split(" "))
start = int(input())
graph  = defaultdict(list)
for _ in range(e):
  u, v, w = map(int, input().split(" "))
  graph[u].append((w, v))

queue = [(0, start)]
dist = defaultdict(int)

while queue:
  time, node = heapq.heappop(queue)
  if node not in dist:
    dist[node] = time
    for cw, cv in graph[node]:
      alt = time + cw
      heapq.heappush(queue, (alt, cv))


for i in range(1,v_num+1):
  if i in dist:
    print(dist[i])
  else:
    print("INF")