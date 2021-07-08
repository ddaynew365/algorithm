
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def main():
    n = int(input())
    nums = list(map(int,input().split()))
    nums.insert(0,0)
    front = [0] * (n+2)
    back = [0] * (n+2)

    for f in range(1,n):
        front[f] = gcd(front[f-1], nums[f])
    for b in range(n,0,-1):
        back[b] = gcd(back[b+1],nums[b])

    ans = -1
    who = 0

    for i in range(n):
        cnt = 0
        if i ==0:
            cnt = back[n-i-3]
        elif i == n-1:
            cnt = front[i-1]
        else:
            cnt = gcd(front[i-1],back[n-2-i])

        num = nums[i]
        if num % cnt == 0: continue
        if ans < cnt:
            ans = cnt
            who = num
    if ans == -1:
        print(ans)
    else:
        print(ans,who)

main()