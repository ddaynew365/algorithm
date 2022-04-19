from collections import defaultdict, deque
import sys
input = sys.stdin.readline
def bfs(start):
  queue = deque([start])
  color = [-1 for _ in range(v+1)]
  color[start] = 0
  
  while queue:
    cur = queue.popleft()
    visit.add(cur)
    for next in graph[cur]:
      if color[next] == -1:
        color[next] = not color[cur] 
        queue.append(next)
      elif color[next] == color[cur]: 
        return False
  return True

t = int(input())
for _ in range(t):
  v, e = map(int, input().split())
  graph = defaultdict(list)
  for _ in range(e):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)
    
  visit = set()
  for start in range(1,v):
    if start in visit:
      continue
    if bfs(start):
      fail = False
    else:
      fail = True
      break
      
  if fail:
    print("NO")
  else:
    print("YES")


