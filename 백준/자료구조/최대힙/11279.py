import heapq
import sys

arr = []

num = int(sys.stdin.readline())

for _ in range(num):
    new = int(sys.stdin.readline())

    if new == 0:
        if arr:
            print(-1 * heapq.heappop(arr))
            continue
        print(0)
    else:
        heapq.heappush(arr, -1*new)


