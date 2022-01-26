from typing import List
from collections import defaultdict
import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        queue = [(0, src, 0)]   
        visited = defaultdict(int)
        for u, v, w in flights:
            graph[u].append((v,w))                                            
        while queue:
            cost, node, count = heapq.heappop(queue)
            if node == dst:
                return cost
            if node not in visited or visited[node] > count:
                visited[node] =count
                if count <= k:
                    for v,w in graph[node]:
                        alt = w + cost
                        heapq.heappush(queue, (alt, v,count+1))
        return -1