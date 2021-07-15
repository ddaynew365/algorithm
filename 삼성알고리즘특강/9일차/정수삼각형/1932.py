"""
다이나믹 프로그래밍을 사용하여 해결하였다. 전형적인 dp 문제로 이차원 리스트를 사용하면 문제없이 풀 수 있는 문제였다.
"""
import sys
n = int(sys.stdin.readline().strip())
graph = []

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().strip().split())))

for i in range(1,n):
    length = len(graph[i])
    for j in range(length):

        if j == 0:
            graph[i][j] = graph[i-1][j] + graph[i][j]
        elif j == length-1:
            graph[i][j] = graph[i-1][j-1] + graph[i][j]
        else:
            graph[i][j] = max(graph[i-1][j-1], graph[i-1][j]) + graph[i][j]
print(max(graph[n-1]))