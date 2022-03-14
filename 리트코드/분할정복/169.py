from collections import Counter, defaultdict
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        answer = 0
        total = len(nums)
    # counter 사용
        # counter = Counter(nums)
   
    # dict로만 사용
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
            
        for num in counter:
            if counter[num] > total // 2:
                answer = num
                
        return answer
        