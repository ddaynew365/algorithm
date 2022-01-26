from typing import List
import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        
        for u,v,w in times:
            graph[u].append([v,w])
            
        Q = [(0,k)]
        dist = defaultdict(list)
        
        while Q:
            time, node = heapq.heappop(Q)
            if node not in dist:
                dist[node] = time
                for v,w in graph[node]:
                    alt = w + time
                    heapq.heappush(Q, (alt, v))
                    
        if len(dist) == n:
            return max(dist.values())
        return -1
                    
        
            
        
            