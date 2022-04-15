n = int(input())
arr = list(map(int, input().split(" ")))
mx,mn = -1e9, 1e9
for num in arr:
  mx = max(num, mx)
  mn = min(num, mn)
  
print(mn, mx)