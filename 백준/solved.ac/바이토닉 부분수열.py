n = int(input())
arr = list(map(int,input().split()))

# 가장 긴 증가하는 부분 수열
up = []
for i in range(n):
  num = arr[i]
  up_max = 0
  for j in range(i):
    if arr[j] < num:
      up_max = max(up_max, up[j])
  up.append(up_max+1)
# 가장 긴 감소하는 부분 수열
down = []
for i in range(n-1,-1,-1):
  num = arr[i]
  down_max = 0
  for j in range(i+1,n):
    if arr[j] < num:
      down_max = max(down_max, down[n-1-j])
  down.append(down_max+1)
print(max([a+b for a,b in zip(up, down[::-1])])-1)