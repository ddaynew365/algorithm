
import sys
from collections import defaultdict
import heapq
prob_num, info_num = map(int,sys.stdin.readline().strip().split())

parent_num = [0] * (prob_num+ 1)
graph= defaultdict(list)

for _ in range(info_num):
    win, lose = map(int, sys.stdin.readline().strip().split())
    graph[win].append(lose)
    parent_num[lose] += 1

queue = []
for i in range(1, prob_num+1):
    if parent_num[i] == 0:
        heapq.heappush(queue, i)
        parent_num[i] = -1


while queue:
    v = heapq.heappop(queue)
    print(v, end = ' ')
    for i in graph[v]:
        parent_num[i] -= 1
        if parent_num[i] == 0:
            heapq.heappush(queue, i)




