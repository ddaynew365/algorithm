# XOR 연산을 사용하여 둘의 비트 차이를 계산 후 bin을 사용하여 문자열로 표현 => count 함수를 사용하여 개수 파악
from typing import List
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        result = bin(x ^ y)
        return result.count('1')