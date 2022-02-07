# 이분탐색에서 lo <= hi라는 조건문은 원소가 1개있을 떄를 고려한 것
# m - 1, m+ 1은 m은 확실히 답이 아니니 뺀 것과 while문을 빠져나갈수있도록 한 것
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        hi = len(nums) - 1
        lo = 0
        
        while lo <= hi:
            m = (lo + hi) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                hi = m - 1
            elif nums[m] < target:
                lo = m + 1
        return -1
        