# 가장 일반적인 방법
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        else:
            return self.fib(n-1) + self.fib(n-2)

# DP 상향식
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
      
# DP 하향식
from collections import defaultdict
class Solution:
    dp = defaultdict(int)
    def fib(self, num: int) -> int:
        if num <= 1:
            return num
        if self.dp[num]:
            return self.dp[num]
        self.dp[num] = self.fib(num-1) + self.fib(num-2)
        return self.dp[num]