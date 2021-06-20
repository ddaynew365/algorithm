import sys
M,N,K = map(int, sys.stdin.readline().strip().split())

while K != 0:
    while M >= 2*N and K != 0:
        K -= 1
        M -= 1
    while M < 2*N and K != 0:
        K -= 1
        N -= 1


if M >= 2*N:
    ans  = N
else:
    ans = M // 2

print(ans)
