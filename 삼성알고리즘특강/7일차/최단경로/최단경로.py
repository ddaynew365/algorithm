import sys, heapq
scan = sys.stdin.readline
N, M = map(int, scan().strip().split())
S = int(scan())

for i in range(M):
    s, e, d = map(int,scan().split())

pq = []
heapq.heappush(pq,[S,0])
print(pq)
