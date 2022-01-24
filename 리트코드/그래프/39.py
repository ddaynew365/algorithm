from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = list()
        
        def dfs(nums, curr, csum):
            if csum < 0 or not nums:
                return
            elif csum == 0:
                result.append(curr)
            
            for i in range(len(nums)):
                dfs(nums[i:],curr+[nums[i]], csum-nums[i])
        
        dfs(candidates, [], target)
        return result