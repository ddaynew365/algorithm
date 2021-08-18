import sys

def confirm(arr, i):
    max = -1
    index = -1
    for j in range(i-1, -1, -1):
        if arr[j] < arr[i]:
            if max < dp[j]:
                max = dp[j]
                index = j
    return index

input = sys.stdin.readline
n = int(input().strip())
arr = list(map(int, input().strip().split()))


dp = [0 for _ in range(n)]
parent = [0 for _ in range(n)]
dp[0] =1
parent[0] = -1
for i in range(1, n):
    j = confirm(arr, i)
    if j == -1:
        dp[i] = 1
        parent[i] = -1
    else:
        dp[i] = dp[j] +1
        parent[i] = j
print(arr)
print(dp)
print(parent)
ans =max(dp)
print(ans)
ans_idx = dp.index(ans)
ans_list = []
while ans_idx != -1:
    ans_list.append(arr[ans_idx])
    ans_idx = parent[ans_idx]

for an in ans_list[::-1]:
    print(an, end =' ')

