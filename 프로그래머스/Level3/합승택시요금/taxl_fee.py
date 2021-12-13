# 참고 코드
# 플로이드-와샬
from math import inf


def solution(n, s, a, b, fares):
    # 0부터 시작하는 인덱스
    s, a, b = s - 1, a - 1, b - 1

    # inf 로 초기화된 거리행렬
    # 자기 자신으로 가는 간선 가중치는 0
    graph = [[inf] * n for _ in range(n)]
    for i in range(n):
        graph[i][i] = 0     

    # 거리행렬에 주어진 비용 넣기
    for fare in fares:
        u, v, w = fare
        graph[u - 1][v - 1] = graph[v - 1][u - 1] = w

    # 플로이드-와샬
    for k in range(n):          # 1. 모든 노드를 중간점(경로)으로 가정하면서
        for i in range(n):      # 2. 거리행렬을 순회
            for j in range(n):  # 3. 현재 거리행렬에 저장된 거리가 k를 거쳐가는 거리보다 멀면 갱신
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
                # graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j]) 시간 거의 두 배 걸림..

    # 출발점을 기준으로 어떤 지점 k를 거쳐 각각 a와 b로 가는 최소 비용을 탐색
    ans = inf
    for k in range(n):
        ans = min(ans, graph[s][k] + graph[k][a] + graph[k][b])

    return ans

# 내가 직접 푼 코드
# 비교해야 될 대상이 2개라면 max, min 보다는 if문을 쓰는 것이 훨씬 효율적
# 모든 노드에서 모든 노드로의 최단 거리 계산은 플로이드 워셜 알고리즘 (N^3 시간 복잡도)
# 한 노드에서 모든 노드로의 최단 거리 계산은 다익스트라 알고리즘
# 다익스트라 알고리즘을 모든 노드에서 사용한 것이 플로이드 워셜과 같은 기능 
    #  -> 하지만 다익스트라 알고리즘은 최적화를 시키면 NlogN이 가능하기 떄문에 더 좋긴하다

def pw(n, fares):
    inf = int(1e9)
    table = [[inf] * (n) for _ in range(n)]
    
    for i in range(n):
        table[i][i] = 0
        
    for i, j, v in fares:
        table[i-1][j-1] = table[j-1][i-1] = v
    
    for num in range(n):
        for i in range(n):
            for j in range(n):
                compare =  table[i][num] + table[num][j]
                if table[i][j] > compare:
                    table[i][j] = compare
    return table

def solution(n, s, a, b, fares):
    s, a, b = s-1, a-1, b-1
    inf = int(1e9)
    table = [[inf] * (n) for _ in range(n)]
    
    for i in range(n):
        table[i][i] = 0
        
    for i, j, v in fares:
        table[i-1][j-1] = table[j-1][i-1] = v
    
    for num in range(n):
        for i in range(n):
            for j in range(n):
                compare =  table[i][num] + table[num][j]
                if table[i][j] > compare:
                    table[i][j] = compare
    answer = int(1e9)
    for i in range(n):
        compare = table[s][i] + table[i][a] + table[i][b]
        if answer > compare:
            answer = compare
    return answer