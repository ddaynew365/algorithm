import sys, heapq
# 입력을 받고
n, k = map(int, sys.stdin.readline().strip().split())
bags = []
jews = []
for _ in range(n):
    m, v = map(int, sys.stdin.readline().strip().split())
    jews.append([m,v])
for _ in range(k):
    bags.append(int(sys.stdin.readline().strip()))

# 가방도 정렬(오름차순
# 보석도 정렬(오름차순)
jews.sort(key = lambda x: (x[0]))
# heapq.heapify(jew)
bags.sort()
# 할 일
# 가방을 크기순으로 보면서, 현재 크기에 넣을 수 있는 가장 적합한 보석을 넣는다.
# 과연이게 맞을지? 가방을 반대로 보면 안될지...고민

maxheap=[]
start = 0
ans = 0

for b in range(k):
    for j in range(start, n):
        # 조건문을 잘 보자
        if bags[b] < jews[j][0]:
            start = j
            break
        if j == n-1:
            start = n
        heapq.heappush(maxheap, -jews[j][1])
    if maxheap:
        ans += -(heapq.heappop(maxheap))
print(ans)

