import sys
sys.setrecursionlimit(1000000)
N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(input()))

for row in graph:
    for char in range(len(row)):
        if row[char] == 'H':
            row[char] = -1
        else:
            row[char] = int(row[char])


ans = 0
max_count = [[-1] * M for _ in range(N)]

dx = [0,0,-1,1]
dy = [1,-1,0,0]


def dfs(y, x, cnt):
    global ans

    if ans < cnt:
        ans = cnt
    if ans > (N*M):
        return 0
    if x < 0 or y < 0 or x >= M or y >= N or graph[y][x] == -1:
        return 0
    mul = graph[y][x]
    if max_count[y][x] >= cnt:
        return 0
    max_count[y][x] = cnt
    for i in range(4):
        dfs(y+ dy[i] * mul, x + dx[i] * mul, cnt + 1)

dfs(0,0,0)
if ans > (N*M):
    print(-1)
else:
    print(ans)

