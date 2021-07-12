from collections import deque
N, M = map(int, input().split())
graph= []
for _ in range(N):
    graph.append(list(map(int,input())))

queue = deque([[0,0]])

while queue:
    y,x = queue.popleft()

    dx = [1,0,-1,0]
    dy = [0,1,0,-1]

    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if new_x < 0 or new_y < 0 or new_x >= M or new_y >= N:
            continue
        if graph[new_y][new_x] == 1:
            graph[new_y][new_x] = graph[y][x] + 1
            queue.append([new_y,new_x])

print(graph[N-1][M-1])

