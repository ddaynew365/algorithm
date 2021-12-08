from collections import deque
import sys

def new_fire_graph(graph, fire):
    g = graph[:]
    f = fire[:]
    for y, x in f[:]:
        for i in range(4):
            newy = y + dy[i]
            newx = x + dx[i]

            if newy < 0 or newx < 0 or newy >= N or newx >= C:
                continue
            if g[newy][newx] == 'J' or g[newy][newx] == '.':
                g[newy][newx] = 'F'
                f.append([newy,newx])
    return g,f

N, C = map(int, sys.stdin.readline().strip().split())
graph = []
fire = []
dy = [1, 0 , -1, 0]
dx = [0, 1, 0 , -1]

for _ in range(N):
    graph.append(list(sys.stdin.readline().strip()))
for idx, val in enumerate(graph):
    if 'J' in val:
        start = [idx, val.index('J')]
    if 'F' in val:
        fire.append([idx, val.index('F')])


queue = deque()
queue.append(start)
graph[start[0]][start[1]] = 1
count = 1
cury, curx = -1 , -1
ans = []

while queue:
    graph, fire = new_fire_graph(graph, fire)
    for i in range(count):
        cury, curx = queue.popleft()
        count -= 1
        if cury == 0 or curx == 0 or cury == N-1 or curx == C-1:
            ans.append(graph[cury][curx])
            break

        for i in range(4):
            nexty, nextx = cury + dy[i], curx + dx[i]
            if nexty < 0 or nextx < 0 or nexty >= N or nextx >= C:
                continue
            if graph[nexty][nextx] == '.':
                graph[nexty][nextx] = graph[cury][curx] + 1
                queue.append([nexty,nextx])
                count += 1

if ans:
    print(min(ans))
else:
    print("IMPOSSIBLE")







