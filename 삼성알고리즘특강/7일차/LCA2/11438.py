import sys
from collections import defaultdict, deque

def find_depth(node):
    depth = [-1] * (n+1)
    queue = deque()
    queue.append(1)
    depth[1] = 0
    while queue:
        cur = queue.popleft()
        for i in child[cur]:
            depth[i] = depth[cur] + 1
            if i == node:
                return depth[node]
            queue.append(i)

child = defaultdict(list)

n = int(sys.stdin.readline().strip())
parent = [0 * (n+1)] * 17 # 입력의 최대값이 100만이기 때문에 logn을 한 것
for _ in range(n-1):
    an, bn = map(int, sys.stdin.readline().strip().split())
    if an < bn:
        child[an].append(bn)
        parent[0][bn] = an
    else:
        child[bn].append(an)
        parent[0][an] =bn
m = int(sys.stdin.readline().strip())

pbs = []

for _ in range(m):
    pba, pbb = map(int, sys.stdin.readline().strip().split())
    pbs.append([pba, pbb])
    depa, depb = find_depth(pba), find_depth(pbb)
    para, parb = pba, pbb

    # while depa > 0 and depb >0:
    #     if depa > depb:
    #         para = parent[para]
    #         depa -= 1
    #     elif depa < depb:
    #         parb = parent[parb]
    #         depb -= 1
    #     else:
    #         para = parent[para]
    #         depa -= 1
    #         parb = parent[parb]
    #         depb -= 1
    #
    #     if para == parb:
    #         ans = para
    #         break
    print(ans)
