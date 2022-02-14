# 파이썬 식으로 푼 풀이과정 bin 함수와 count 함수를 사용하여 쉽게 풀 수 있다.
from typing import List
class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')

# 좀 더 범용적으로 푼 풀이과정-> 해당값과 해당값-1을 and 연산하면 1이 하나씩 빠진다 -> n이 0이 될 때까지 반복하며 count 값 구하기
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0 
        while n != 0:
            n &= n-1
            count += 1
        return count