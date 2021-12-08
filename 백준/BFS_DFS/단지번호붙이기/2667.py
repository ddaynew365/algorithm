from collections import deque

def bfs(start):
    queue = deque([start])
    num = 0
    graph[start[0]][start[1]] = count
    while queue:
        cy, cx = queue.popleft()
        num += 1

        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]
            if ny < 0 or ny >=N or nx < 0 or nx >= N:
                continue
            if graph[ny][nx] == 1:
                graph[ny][nx] = count
                queue.append([ny, nx])

    return num


N = int(input())
graph = []
dy = [0,1,0,-1]
dx = [1,0,-1,0]
house = []
count = 2
for _ in range(N):
    graph.append(list(map(int,list(input()))))

for y in range(N):
    for x in range(N):
        if graph[y][x] != 1:
            continue
        house.append(bfs([y, x]))
        count += 1

print(count-2)
for i in sorted(house):
    print(i)