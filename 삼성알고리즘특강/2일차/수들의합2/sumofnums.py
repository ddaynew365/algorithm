N, M = map(int, input().split())
arr = list(map(int, input().split()))

sum = 0
left = 0
answer = 0
for right in arr:
    sum += right
    while sum > M:
        sum -= arr[left]
        left += 1
    if sum == M:
        answer += 1

print(answer)