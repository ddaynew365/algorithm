import sys
sys.setrecursionlimit(1000000)
N, M = map(int,input().split())
graph =[]
# DP 방법을 사용하여 연산 줄임
max_count =[[-1]* M for _ in range(N)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
# 전역변수(답)
ans = 0
# 데이터 받고
for _ in range(N):
    graph.append(list(input()))

for i in graph:
    for j in range(len(i)):
        if i[j] == 'H':
            i[j] = -1
        else:
            i[j] =int(i[j])

# 재귀 함수
def dfs(y, x, cnt):
    global ans
    if ans < cnt:
        ans = cnt
    if ans > (N * M):
        return 0

    if y < 0 or x < 0 or y >= N or x >= M or graph[y][x] == -1:
        return 0

    if cnt <= max_count[y][x]:
        return 0

    max_count[y][x] = cnt
    mul = graph[y][x]
    for i in range(4):
        dfs(y + dy[i] * mul, x + dx[i] * mul, cnt + 1)

dfs(0,0,0)
if ans > (N*M):
    ans = -1
print(ans)


