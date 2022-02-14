from typing import List
class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        INT_MAX = 0x7FFFFFF
        while b!= 0:
            a,b = (a^b) & MASK, ((a&b)<<1) & MASK
            
        if a > INT_MAX:
            a = ~(a ^ MASK)
        return a