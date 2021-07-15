import sys
input =sys.stdin.readline
n, m = map(int, input().split())
arr = [0] + list(map(int, input().strip().stplit()))

for i in range(1,n+1):
    dp[i]=