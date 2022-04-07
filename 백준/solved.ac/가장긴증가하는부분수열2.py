n = int(input())
arr = list(map(int, input().split()))

Lis = []
answer = []
for num in arr:
  if not Lis or Lis[-1] < num:
    Lis.append(num)
    answer.append(num)
  elif Lis[-1] > num:
    lo = 0
    hi = len(Lis)
    while lo <= hi:
      mid = (lo + hi) // 2
      if Lis[mid] == num:
        break
      elif Lis[mid] > num:
        hi = mid - 1
      else:
        lo = mid + 1
    Lis[lo] = min(Lis[lo], num)

print(len(Lis))
print(' '.join(map(str,Lis)))
    
