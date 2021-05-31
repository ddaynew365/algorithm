import sys
# 사용자 입력
n, m = map(int,sys.stdin.readline().split())
height= list(map(int,sys.stdin.readline().split()))
# 초기화
left = 1
right = max(height)
ans = 0
# 이분탐색
while left <= right:
    count = 0
    mid = (left + right) // 2
    for i in height:
        if i > mid:
            count += (i - mid)
        if count > m:
            break

    if count >= m:
        ans = max(ans, mid)
        left = mid + 1
    else:
        right = mid - 1

print(ans)






