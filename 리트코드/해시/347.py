# 힙으로 푸는 방법=> Counter를 쓴 후 최대 힙에 숫자들을 집어놓고 순서대로 꺼낸다.
from collections import Counter
from typing import List
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        heap = []
        count = Counter(nums)
        for num in count:
            heapq.heappush(heap, (-count[num], num))
        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        return result

# 파이썬틱한 방법 => zip은 리스트 여러개를 하나씩 꺼내서 새로운 리스트를 여러개 만드는 것, *는 unpack하는 방법
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return list(zip(*Counter(nums).most_common(k)))[0]
