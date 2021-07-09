import sys, heapq
n, k = map(int, sys.stdin.readline().strip().split())
bag = []
jew = []
for _ in range(n):
    m, v = map(int, sys.stdin.readline().strip().split())
    jew.append([m,v])
for _ in range(k):
    bag.append(int(sys.stdin.readline().strip()))
# 입력을 받고
# 가방도 정렬(오름차순
# 보석도 정렬(오름차순)
# 할 일
# 가방을 크기순으로 보면서, 현재 크기에 넣을 수 있는 가장 적합한 보석을 넣는다.
# 과연이게 맞을지? 가방을 반대로 보면 안될지...고민
jew.sort(key = lambda x : (x[0]))
heapq.heapify(jew)
bag.sort()

_sum = 0
for b in bag:
    for j in range(len(jew)):
        m,v = jew[j]
        if m > b:
            if j == 0:
                break
            _sum += jew[j-1][1]
            jew[j-1][0] =100000000
            break

print(_sum)