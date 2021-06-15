# 가장 기본적인 다익스트라 알고리즘- 시간 복잡도가 O(V^2)으로 노드의 개수(V)가 5000개 이상만 되어도 걸리는 시간이 
from collections import Counter
INF = int(1e9)

def get_smallest_node(distance, visited,n):
    min_value = INF
    index = 0
    
    for i in range(1,n+1):
        if distance[i] < min_value and visited[i] == False:
            min_value = distance[i]
            index = i
    return index
    
def dijkstra(start, distance, visited, edge,n):
    distance[start] = 0
    visited[start] = True
    for i in edge:
        if start == i[0]:
            distance[i[1]] = 1
        elif start == i[1]:
            distance[i[0]] = 1
            
    for _ in range(n-1):
        now = get_smallest_node(distance, visited,n)
        visited[now]= True
        
        for j in edge:
            if now == j[0]:
                cost = distance[now] +1
                if cost < distance[j[1]]:
                    distance[j[1]] = cost
            elif now == j[1]:
                cost = distance[now] +1
                if cost < distance[j[0]]:
                    distance[j[0]] = cost
                    
    for i in range(len(distance)):
        if distance[i] == INF:
            distance[i] = -1
            
    return distance
            
                
def solution(n, edge):
    answer = 0
    distance= [INF] * (n+1)
    visited = [False] *(n+1)
    start = 1
    distance = dijkstra(start, distance, visited, edge,n)
    
    max_ = max(distance)
    count = dict(Counter(distance))
    answer = count[max_]
    
    return answer
  
  
  
  
#==================================================================
# 두 번째로 우선순위 큐를 사용한 다익스트라 알고리즘- 조금 더 시간 복잡도가 개선되었지만 문제에서 주어진 시간에 맞추질 못했다 
#  생각해본 결과 weight가 모두 1인 상황에서는 다익스트라 알고리즘을 사용하는 것이 비효율적이라는 결론을 냈다.
#  이런 상황에서는 bfs 알고리즘을 사용하는 것이 낫다고 판단하였다.
from collections import Counter
import heapq
INF = int(1e9)

    
def dijkstra(start, distance, edge,n):
    q = []
    heapq.heappush(q, (0,start))
    distance[start] = 0
            
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        
        for i in edge:
            if now == i[0]:
                cost = dist + 1
                if cost < distance[i[1]]:
                    distance[i[1]] = cost
                    heapq.heappush(q, (cost,i[1]))
            elif now == i[1]:
                cost = dist + 1
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost,i[0]))
            
    for i in range(len(distance)):
        if distance[i] == INF:
            distance[i] = -1
            
    return distance
            
                
def solution(n, edge):
    answer = 0
    distance= [INF] * (n+1)
    start = 1

    distance = dijkstra(start, distance, edge,n)

    max_ = max(distance)
    count = dict(Counter(distance))
    answer = count[max_]
    
    return answer

#================================================================
# 3 번쨰는 bfs 알고리즘을 사용하였다. 처음에는 주어진 edge 리스트를 그대로 사용해보았지만 그렇게 되면 bfs 알고리즘의 for문이 굉장히 비효율적으로 되었다
# 따라서 graph라는 새로운 리스트를 만들어서 구현하였다. 그 결과 복잡한 테스트의 경우 20배 빠른 속도를 보여주었다.
from collections import deque

def bfs(n, graph, start):
    distance = [-1] * (n+1)
    distance[start] = 0
    
    queue = deque()
    queue.append(start)
    
    while queue:
        v = queue.popleft()
        
        for i in graph[v]:
            if distance[i]  == -1:
                distance[i] = distance[v]  + 1
                queue.append(i)
    return distance
    
def solution(n, edge):
    answer = 0

    graph = [ [] for _ in range(n + 1)]
    for f, to in edge:
        graph[f].append(to)
        graph[to].append(f)
        
    distance = bfs(n, graph, 1)
    answer = distance.count(max(distance))
    return answer
