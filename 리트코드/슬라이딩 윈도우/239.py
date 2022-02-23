from collections import deque
from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n*k ==0:
            return nums
        
        Q = deque()
        
        def clear(i):
            if Q and Q[0] == i-k:
                Q.popleft()
                
            while Q and nums[Q[-1]] < nums[i]:
                Q.pop()
        
        for i in range(k):
            clear(i)
            Q.append(i)
        
        result = [nums[Q[0]]]
        
        for i in range(k,n):
            clear(i)
            Q.append(i)
            result.append(nums[Q[0]])
            
        return result

sol = Solution()
a = sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7],3)
print(a)