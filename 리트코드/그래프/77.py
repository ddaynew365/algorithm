from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = list()
        nums = [i+1 for i in range(n)]
        def dfs(nums, curr):
            if len(curr) >= k:
                result.append(curr)
                return
            for i in range(len(nums)):
                dfs(nums[i+1:], curr+[nums[i]])
        
        dfs(nums, [])
        return result
            
        