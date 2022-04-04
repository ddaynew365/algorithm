from bisect import bisect_left
n = int(input())
arr = list(map(int, input().split()))

lis = []
for num in arr:
  if not lis:
    lis.append(num)
    continue
  if lis[-1] < num:
    lis.append(num)
  elif lis[-1] > num:
    # mid = bisect_left(lis, num)
    low = mid = 0
    hi = len(lis)
    while low <= hi:
      mid =(low + hi) //2
      if lis[mid] == num:
        break
      elif lis[mid] > num:
        hi = mid - 1
      elif lis[mid] < num:
        low = mid + 1
    lis[low] = min(lis[low], num)
print(len(lis))
      