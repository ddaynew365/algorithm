import sys
from collections import defaultdict
input = sys.stdin.readline
t = int(input())
for _ in range(t):
  n, k = map(int, input().split())
  answer = 0
  c_time = [0]
  c_time += list(map(int, input().split()))
  c_rule = defaultdict(list)
  c_count = defaultdict(int)
  t_time = defaultdict(int)
  
  for _ in range(k):
    start, end = map(int, input().split())
    c_rule[start].append(end)
    c_count[end] += 1
  w = int(input())
  
  stack = []
  for i in range(1,n+1):
    if c_count[i] == 0:
      stack.append([0,i])
      c_count[i] = -1

  while stack:
    total_time, cur = stack.pop()
    c_count[cur] = -1
    time = c_time[cur]
    if cur == w:
      print(total_time+time)
      break
    for next in c_rule[cur]:
      c_count[next] -= 1
      # 이 부분이 중요
      t_time[next] = max(t_time[next], total_time + time)
      if c_count[next] == 0:
        stack.append([t_time[next] ,next])