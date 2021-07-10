n, m ,k = map(int, input().split())

cache = [[-1] * m for _ in range(n)]
answer =[]
counta =n
countz =m
for i in range(n+m):
    tmp = getaz(counta-1, countz)
def getaz(a,z):
    if a ==0 or z== 0:
        return 1
    if cache[a][z] != -1:
        return cache[a][z]

    return cache[a][z] = (getaz(a-1, z) + getaz(a,z-1))