from collections import deque
from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        n = len(nums)
        if n*k == 0 or k == 1:
            return nums
        
        def clear(i):
            if queue and queue[0] == i-k:
                queue.popleft()
            
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            
        for i in range(k):
            clear(i)
            queue.append(i)
        
        result = [nums[queue[0]]]
        for i in range(k, n):
            clear(i)
            queue.append(i)
            result.append(nums[queue[0]])
        
        return result

sol = Solution()
a = sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7],3)
print(a)