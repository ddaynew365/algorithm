"""
이번 문제는 다이나믹 프로그래밍 알고리즘의 대표 유형이었다. 모든 칸을 완전탐색하여 자신의 위와 왼쪽칸 중 더 숫자가
높은 칸을 선택하여 자기 자신칸의 수와 더해주면서 (N,M)에 도달하면 문제가 해결되었다. 처음에는 문제에 적힌 조건대로
(N-1,M-1)도 고려해주었지만 나중에 생각해보니 (N,M-1), (N-1,M)에 모두 포함된다는 것을 알게 되었다.
"""
import sys

N, M = map(int, sys.stdin.readline().strip().split())
graph = [[0 for _ in range(M+1)]]
for n in range(N):
    graph.append([0]+list(map(int, sys.stdin.readline().strip().split())))

for n in range(1, N+1):
    for m in range(1, M+1):
        # graph[n][m] = max(graph[n-1][m], graph[n][m-1], graph[n-1][m-1]) + graph[n][m]
        graph[n][m] = max(graph[n - 1][m], graph[n][m - 1]) + graph[n][m]
print(graph[N][M])