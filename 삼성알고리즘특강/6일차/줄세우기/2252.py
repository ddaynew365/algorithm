from collections import deque, defaultdict
import sys

n,m = map(int,sys.stdin.readline().strip().split())
graph = defaultdict(list)
indegree = [0 for _ in range(n+1)]

for _ in range(m):
    parent, child = map(int,sys.stdin.readline().strip().split())
    graph[parent].append(child)
    indegree[child] += 1

queue = deque()

for i in range(1,n+1):
    if indegree[i] == 0:
        queue.append(i)

while queue:
    cur = queue.popleft()
    print(cur, end =' ')
    for g in graph[cur]:
        indegree[g] -= 1
        if indegree[g] == 0:
            queue.append(g)

