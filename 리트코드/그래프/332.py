from typing import List
from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        n = len(tickets) + 1
        schedule = defaultdict(list)
        for fro, to in tickets:
            schedule[fro].append(to)
        result = list()

        
        def dfs(curr, start):
            if result:
                return
            if len(curr) == n:
                result.append(curr)
                return
            for dest in sorted(schedule[start]):
                schedule[start].remove(dest)
                dfs(curr + [dest], dest)
                schedule[start].append(dest)
        
        dfs(["JFK"], "JFK")
        return result[0]
            
                