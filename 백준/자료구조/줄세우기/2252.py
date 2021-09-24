"""
이번 문제를 처음으로 위상정렬 알고리즘을 구현해보았다. 큐의 형태로 구현하니 bfs 알고리즘과
유사함을 느껴 상대적으로 쉽게 구현하였다.
"""
import sys
from collections import defaultdict, deque

st_num, comp = map(int,sys.stdin.readline().strip().split())
result = defaultdict(list)
parent = [0] * (st_num+1)

for _ in range(comp):
    win, lose = map(int,(sys.stdin.readline().strip().split()))
    parent[lose] += 1
    result[win].append(lose)

queue = deque()
answer = []

for i in range(1,st_num+1):
    if parent[i] == 0:
        queue.append(i)

while queue:
    v = queue.popleft()
    answer.append(v)
    for i in result[v]:
        parent[i] -= 1
        if parent[i] == 0:
            queue.append(i)

for i in answer:
    print(i ,end = ' ')