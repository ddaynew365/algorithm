import sys, heapq
N = int(sys.stdin.readline().strip())
minpq = []
maxpq = []
for idx in range(N):
    a = int(sys.stdin.readline().strip())
    if len(minpq) == len(maxpq):
        heapq.heappush(maxpq, -a)
    else:
        heapq.heappush(minpq, a)

    if minpq and maxpq and minpq[0] < -maxpq[0]:
        min_value = heapq.heappop(minpq)
        max_value = heapq.heappop(maxpq)
        heapq.heappush(minpq, -max_value)
        heapq.heappush(maxpq, -min_value)
    print(-maxpq[0])
