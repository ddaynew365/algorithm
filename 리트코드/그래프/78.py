from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = list()
        
        def dfs(nums, curr, n):
            if n == 0:
                result.append(curr)
                return
            for i in range(len(nums)):
                dfs(nums[i+1:], curr + [nums[i]], n-1)
        
        for i in range(len(nums)+1):
            dfs(nums, [], i)
            
        return result