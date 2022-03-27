import sys
n = int(input())
wait = list(map(int,sys.stdin.readline().strip().split(" ")))

wait.sort()

wait_time = []
cur = 0
for p in wait:
  wait_time.append(cur+p)
  cur += p
print(sum(wait_time))