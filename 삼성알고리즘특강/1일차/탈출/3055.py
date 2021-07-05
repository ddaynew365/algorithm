from collections import deque
import sys

def water_graph(graph, water):
    g = graph[:]
    w = water[:]
    for y, x in w[:]:
        for i in range(4):
            newy = y + dy[i]
            newx = x + dx[i]
            if newy < 0 or newx < 0 or newy >= N or newx >= C:
                continue
            if g[newy][newx] == '.' or g[newy][newx] == 'S':
                g[newy][newx] = '*'
                w.append([newy, newx])
    return g, w

N, C = map(int, sys.stdin.readline().strip().split())
graph = []
water = []
rock = []
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
for _ in range(N):
    graph.append(list(sys.stdin.readline().strip()))

for idx,val in enumerate(graph):
    if 'S' in val:
        start = [idx,val.index('S')]
    if 'D' in val:
        desti = [idx,val.index('D')]
    if '*' in val:
        water.append([idx,val.index('*')])

queue =deque()
queue.append(start)
graph[start[0]][start[1]] = 0
count = 1
while queue:
    graph, water = water_graph(graph, water)
    for i in range(count):
        cury, curx = queue.popleft()
        count -= 1
        if [cury, curx] == desti:
            break

        for i in range(4):
            nexty, nextx = cury+dy[i], curx+dx[i]
            if nexty < 0 or nextx < 0 or nexty >= N or nextx >= C:
                continue
            if graph[nexty][nextx] == '.' or graph[nexty][nextx] == 'D':
                graph[nexty][nextx] = graph[cury][curx] + 1
                queue.append([nexty, nextx])
                count += 1

ansy, ansx = desti
if graph[ansy][ansx] == 'D':
    print('KAKTUS')
else:
    print(graph[ansy][ansx])



