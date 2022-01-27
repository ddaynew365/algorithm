from typing import List
import heapq
# heap을 사용하여 최대 힙으로 구현
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minus_nums = [i*-1 for i in nums]
        heapq.heapify(minus_nums)
        for _ in range(k-1):
            heapq.heappop(minus_nums)
        return -1 * heapq.heappop(minus_nums)
      

# 이러한 방법도 가능하다
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]