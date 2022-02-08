import sys
import heapq
from collections import defaultdict, deque

def cabin(start, graph):
  visit = list()
  queue = deque([[start, 0]])
  _sum = 0
  while queue:
    cur, count = queue.popleft()
    visit.append(cur)
    _sum += count
    for i in graph[cur]:
      if i not in visit:
        queue.append([i, count + 1])

  return _sum

n, m = map(int,sys.stdin.readline().split())
graph = defaultdict(list)
for _ in range(m):
  a, b = map(int,sys.stdin.readline().split())
  graph[a].append(b)
  graph[b].append(a)

num = list()
## 정렬을 사용한 방법 96ms
# for i in range(1,n+1):
#   num.append([i, cabin(i, graph)])
  
# num.sort(key = lambda x:[x[1],x[0]])
# print(num[0][0])

## 힙을 사용한 방법 88ms
for i in range(1,n+1):
  heapq.heappush(num, [cabin(i,graph),i])
  
print(heapq.heappop(num)[1])