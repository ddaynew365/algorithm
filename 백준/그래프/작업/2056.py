from collections import defaultdict, deque
import sys
n = int(sys.stdin.readline())
times = [0]
graph = defaultdict(list)
indegree =[0 for _ in range(n+1)]
indegree[0] = -1
for i in range(1, n+1):
  time, num, *starts = map(int, sys.stdin.readline().split())
  times.append(time)
  if num != 0:
    for start in starts:
      graph[start].append(i)
      indegree[i] += 1
      
answer =[0 for _ in range(n+1)]
answer[1] = times[1]
queue = deque([1])
indegree[1] = -1
while queue:
  cur = queue.popleft()
  for i in graph[cur]:
    indegree[i] -= 1
  for idx, val in enumerate(indegree):
    if val == 0:
      queue.append(idx)
      answer[idx] = max(answer[idx], answer[cur]+times[idx])
      indegree[idx] = -1
      
print(max(answer))