N, M = map(int,input().split())

count = 1
if N == 2:
    count += ((M-1) // 2)
    if count > 4:
        count = 4
elif N ==1 or M ==1:
    count = 1
elif M < 7:
    count = M
    if count >4:
        count = 4
else:
    count = M-2
print(count)