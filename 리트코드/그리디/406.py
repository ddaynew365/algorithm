# 우선순위큐를 활용한 방법
# 이 문제의 경우, 키가 큰 사람부터 줄을 세우면 나중에 자신보다 키 큰 사람의 수를 셀 필요가 없어진다
# 따라서 우선순위큐를 통해 키큰 사람부터 세우고 [1]의 값은 인덱스로 사용한다.
import heapq
from typing import List
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        max_pri = []
        answer = []
        for p in people:
            p[0] *= -1
            heapq.heappush(max_pri,p)
        
        while max_pri:
            p = heapq.heappop(max_pri)
            answer.insert(p[1],[-1*p[0],p[1]])
        return answer