import sys
from collections import defaultdict, deque
st_num, comp = map(int,sys.stdin.readline().strip().split())
result = defaultdict(list)

parent = [0] * (st_num+1)
for _ in range(comp):
    win , lose = map(int,(sys.stdin.readline().strip().split()))
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
