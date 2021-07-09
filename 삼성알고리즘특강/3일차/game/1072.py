X, Y = map(int, input().split())

curZ = Y // X

if curZ == 99 or curZ == 100:
    print(-1)
else:
    left = 0
    right = 100000000
    while True:
        mid = (left + right) // 2
        nextZ = (Y + mid)//(X + mid)

        if neztZ > curZ:

        else:
            left = mid + 1




