import sys
input = sys.stdin.readline

def union(a,b):
  root_a = find(a)
  root_b = find(b)
  arr[root_b] = root_a
  return

def find(num):
  if num == arr[num]:
    return num
  else:
    pnum = find(arr[num])
    arr[num] = pnum
    return pnum

n, m = map(int, input().split())
arr = [i for i in range(n+1)]
for _ in range(m):
  cmd, a, b = map(int, input().split(" "))
  if cmd == 0:
    union(a,b)
  else:
    print("YES") if find(a) == find(b) else print("NO")