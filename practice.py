from collections import defaultdict
import sys, heapq
input = sys.stdin.readline
v_num, e_num = map(int, input().split(" "))
start = int(input())
graph = defaultdict(list)
for _ in range(e_num):
  a, b, c=  map(int, input().split(" "))
  graph[a].append((c,b))
  
queue = [(0,start)]
dist = defaultdict(int)
while queue:
  weight, node = heapq.heappop(queue)
  if node not in dist:
    dist[node] = weight
    for cw, cv in graph[node]:
      alt = weight + cw
      heapq.heappush(queue, (alt, cv))

for i in range(1, v_num+1):
  if i in dist:
    print(dist[i])
  else:
    print("INF")