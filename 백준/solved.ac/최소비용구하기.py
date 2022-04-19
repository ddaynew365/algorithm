import sys
from collections import defaultdict
from heapq import heappush, heappop
input = sys.stdin.readline
# 이렇게 변수를 미리 지정해주니 4ms 더 빨랐다
INF = int(1e9)
n = int(input())
m = int(input())
graph = defaultdict(list)
for _ in range(m):
  start , end , cost = map(int, input().split())
  # 리스트 대신 튜플을 사용하니 200ms 더 빨랐다
  graph[start].append((end, cost))
start, end = map(int, input().split())

# 다익스트라
dist = [INF] * (n+1)
queue = []
heappush(queue, (0, start))
while queue:
  total_cost, cur = heappop(queue)
  # 이전 노드에서 31번째 줄에 이미 최단거리를 dist[노드]에 넣어줬기 때문에 < 대신 <= 를사용하면 그 최단거리인 경우도 스킵된다.
  if dist[cur] < total_cost:
    continue
  for next, cost in graph[cur]:
    ncost = cost + total_cost
    # <를 사용하면 메모리 초과가 났었는데 <=를 사용하면 성공했다
    # 다익스트라 사용시 주의
    if dist[next] <= ncost:
      continue
    dist[next] = ncost
    heappush(queue,(ncost, next))

print(dist[end])
