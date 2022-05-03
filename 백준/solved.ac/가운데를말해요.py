from heapq import heappush,heappop
import sys
input = sys.stdin.readline
n = int(input())
down = []
up = []
mid = None
answer = []
for _ in range(n):
  num = int(input())
  # 초기 세팅
  if not mid:
    mid = num
    answer.append(mid)
    # print(mid)
    continue
  elif not up:
    heappush(up, max(mid,num))
    mid = min(num, mid)
    answer.append(mid)
    # print(mid)
    continue
  # 실질 로직
  if len(down) == len(up):
    temp = sorted([mid, num, -heappop(down)])
  else:
    temp = sorted([mid, num, heappop(up)])
  heappush(down, -temp[0])
  mid = temp[1]
  heappush(up, temp[2])
  answer.append(mid)
  print(down, mid, up)
  # print(mid)

for i in answer:
  print(i)