n = int(input())
k = int(input())
lo = 1
hi = n*n
while lo <= hi:
  mid = (lo + hi) // 2
  val = 0
  for i in range(1,n+1):
    val += min(mid//i, n)
  if val >= k:
    hi = mid - 1
  else:
    lo = mid + 1
print(lo)
    