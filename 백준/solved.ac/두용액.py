n = int(input())
arr = sorted(list(map(int, input().split())))

lo, hi = 0, n-1
answer = abs(arr[lo]+arr[hi])

ans_lo = arr[lo]
ans_hi = arr[hi]

while lo < hi:
  total = arr[lo] + arr[hi]
  if abs(total) < answer:
    ##
    # ans_lo, ans_hi = lo,hi
    ans_lo, ans_hi = arr[lo],arr[hi]
    ##
    answer = abs(total)
    if answer == 0:
      break
  if total > 0:
    hi -= 1
  elif total < 0:
    lo += 1
##
# print(arr[ans_lo], arr[ans_hi])
print(ans_lo, ans_hi)
##
