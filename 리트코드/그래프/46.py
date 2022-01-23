from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = list()
        def dfs(clist, origin):
            if not origin:
                result.append(clist)
            for num in range(len(origin)):
                dfs(clist+[origin[num]], origin[:num] + origin[num+1:])
        dfs([], nums)
        return result
    
