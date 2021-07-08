a, b = map(int, input().split())
c, d = map(int, input().split())

e = a*d +b*c
f = b*d

# 최대공약수
def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x%y)


g = gcd(e, f)
print(e//g,f//g)

