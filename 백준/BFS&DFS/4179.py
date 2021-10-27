from collections import deque
import sys


def new_fire_graph(graph, fire):
    g = graph[:]
    f = fire[:]
    for y, x in f[:]:
        for i in range(4):
            newy = y + dy[i]
            newx = x + dx[i]

            if(newy < 0 or newx < 0 or newy >= )

    return

N, C = map(int, sys.stdin.readline().strip().split())
graph = []
fire = []
dy = [1, 0 , -1, 0]
dx = [0, 1, 0 , -1]

for _ in range(N):
    graph.append(list(sys.stdin.readline().strip()))

for idx, val in enumerate(graph):
    if 'J' in val:
        start =






