import sys
n, h = map(int, input().split())
sum =[0] * (h+1)
for i in range(n):
    bar = int(sys.stdin.readline().strip())
    if i % 2 == 0:
        sum[h-bar + 1] += 1
    else:
        sum[1]+= 1
        sum[bar + 1] -= 1

answer = 1e9
count = 0
for j in range(1,h+1):
    sum[j] += sum[j-1]
    if answer > sum[j]:
        answer = sum[j]
        count = 1
    elif sum[j] == answer:
        count += 1
print(answer, count)
