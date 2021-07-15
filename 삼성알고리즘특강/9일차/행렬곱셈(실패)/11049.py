"""
그리디 방식이 틀려나? -> 현재의 최적해가 미래의 최적해인지는 확정이 안되기 떄문에
부적절하다고 판단
다음에는 DP로 풀어보는 방식을 사용해 봐야겠다.
"""
import sys
input =sys.stdin.readline
n = int(input().strip())
arrs =[]
for _ in range(n):
    arrs.append(list(map(int, input().strip().split())))


def dp(arrs, ans):
    if len(arrs) == 1:
        return ans
    min = 1e9
    for i in range(len(arrs)-1):
        new = arrs[i][0] * arrs[i+1][1]
        if new < min:
            min = new
            find = i
            mid = arrs[i][1]
        elif new == min:
            if arrs[i][1] < mid:
                min = new
                find = i
                mid = arrs[i][1]
    a, b = arrs.pop(find)
    c, d = arrs.pop(find)
    arrs.insert(find,[a,d])
    ans += a * b * d
    return dp(arrs,ans)


print(dp(arrs, 0))
