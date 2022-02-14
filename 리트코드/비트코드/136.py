# XOR 연산으로 2번 중복되는 수가 오면 없어지면 한번만 오는 수가 남게되는 성질을 이용
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        
        return result