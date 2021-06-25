"""
실패 - 시간 초과 -> 시간초과를 줄이는 방법을 생각해봐야 할듯
"""
import sys
from collections import deque
N, K, M = map(int, sys.stdin.readline().strip().split())
hy_graph= []
for m in range(M):
    hy_graph.append(list(map(int,sys.stdin.readline().strip().split())))

queue =deque()
start = [1, 1]
queue.append(start)
visited = set([1])
found = False

while queue:
    dist, station = queue.popleft()

    if station == N:
        print(dist)
        found =True
        break
    for path in hy_graph:
        if station in path:
            for hy in path:
                if hy not in visited:
                    queue.append([dist+ 1, hy])
                    visited.add(hy)
if found == False:
    print(-1)