n, k = map(int,input().split())
num = list()
for i in range(n):
    num.append(int(input()))
count = 0
left = 1
right = max(num)
mid = 0
ans = 0

while left <= right:
    count = 0
    mid = (left + right) // 2

    if mid == 0:
        ans = 1
        break

    for j in num:
        count += (j // mid)

    if count >= k:
        ans = max(ans, mid)
        left = mid + 1

    else:
        right = mid - 1


print(ans)
