import sys
from heapq import heappush, heappop
from collections import defaultdict 
input = sys.stdin.readline
v, e = map(int, input().split())
graph = defaultdict(list)
elist = []
for _ in range(e):
  a, b, c = map(int, input().split())
  heappush(elist, [c,a,b])

arr = [i for i in range(v+1)]
def union(a, b):
  pa = find(a)
  pb = find(b)
  arr[pa] = pb
  
def find(num):
  if num == arr[num]:
    return num
  p = find(arr[num])
  arr[num] = p
  return p

edge = 0
answer = 0
while edge != (v-1):
  w, a, b = heappop(elist)
  if find(a) != find(b):
    union(a,b)
    answer += w
    edge += 1
  
print(answer)