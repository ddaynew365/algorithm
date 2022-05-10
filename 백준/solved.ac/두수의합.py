n = int(input())
arr = list(map(int, input().split()))
x = int(input())
arr.sort()
total = 0
count = 0
# # 이분탐색
# start, end = 0, 1
# while end < n:
#   lo, hi = 0, end-1
#   while lo <= hi:
#     mid = (lo+hi) // 2
#     val = arr[mid] + arr[end]
#     if val > x:
#       hi = mid - 1
#     elif val < x:
#       lo = mid + 1
#     else:
#       count += 1
#       break
#   end += 1

# 투 포인터
start, end = 0, n-1
count = 0
while start < end:
  total = arr[start] + arr[end]
  
  if total > x:
    end -= 1
  elif total < x:
    start += 1
  else:
    start += 1
    end -= 1
    count += 1
    
print(count)