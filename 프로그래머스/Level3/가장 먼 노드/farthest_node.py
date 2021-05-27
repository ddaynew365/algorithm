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
