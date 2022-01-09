# Counter, dict, defaultdict 즉 해시를 이용하여 stones의 각 원소들의 개수를 센후 jewels애서
# 해당 값들의 원소 개수를 더해 값을 반환하는 방식
from collections import Counter
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        num_b = Counter(stones)
        answer = 0
        for i in jewels:
            answer += num_b[i]
        return answer