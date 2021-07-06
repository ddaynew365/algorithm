N , S = map(int,input().split())
arr = list(map(int, input().split()))

min_len = 1e9
sum = 0
left = 0
for right in range(len(arr)):

    sum += arr[right]
    while sum >= S:
        if min_len > (right - left + 1):
            min_len = (right - left + 1)
        sum -= arr[left]
        left += 1

if min_len == 1e9:
    print(0)
else:
    print(min_len)