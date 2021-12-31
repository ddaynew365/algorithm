# 주식을 사고팔기 가장 좋은 시점
# 해당 문제는 각인덱스마다 저점을 구하여 현재인덱스의 값과 비교해가며 저점과 최대 이득을 최신화하는 방향으로
# 문제를 풀면된다. 이렇게 하면 O(N)의 시간복잡도밖에 걸리지 않는다.
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        low, max_value = prices[0], 0
        for i in range(1, len(prices)):
            cur_value = prices[i] - low
            if cur_value > max_value:
                max_value = cur_value
            if low > prices[i]:
                low = prices[i]
        return max_value
        