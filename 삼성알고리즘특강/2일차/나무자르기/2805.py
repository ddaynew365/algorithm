N, M = map(int, input().split())
arr = list(map(int, input().split()))

right = max(arr)
left = 0
ans =0
while(left <= right):
    mid = (left + right) // 2
    s = 0
    for i in arr:
        if i <= mid:
            continue
        else:
            s += (i - mid)
        if s > M:
            break

    if s < M:
        right = mid - 1
    elif s >= M:
        ans = max(ans, mid)
        left = mid + 1

print(ans)