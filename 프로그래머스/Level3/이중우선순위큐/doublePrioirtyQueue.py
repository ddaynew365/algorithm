'''
첫번째 방법 - 단순 리스트를 사용하여 값이 들어오면 정렬을 하는 방법 - 이번 문제의 테스트 케이스가 너무 빈약해 오히려 아래보다 시간이 빠르다. 시간복잡도는 더 크다.
'''
from collections import deque
def solution(operations):
    answer = []
    ans = []
    for i in operations:
        com, val = i.split(' ')
        val = int(val)
        
        if com == 'D' and answer:
            if val == 1:
                answer.pop()
            else:
                answer.pop(0)
        elif com == 'I':
            answer.append(val)
            answer.sort()
        
    if answer:
        return [answer[-1], answer[0]]
    else:
        return [0,0]
        
'''
두번째 방법 - 힙을 사용한 방법이다. min heap을 사용하여 최솟값을 구하고 최댓값은 heapq모듈의 nlargest()함수를 사용하여 구하였다.
'''

import heapq
def solution(operations):
    answer = []
    ans = []
    for i in operations:
        com, val = i.split(' ')
        val = int(val)
        
        if com == 'D' and answer:
            if val == 1:
                answer = heapq.nlargest(len(answer),answer)[1:]
                heapq.heapify(answer)
            else:
                heapq.heappop(answer)
        elif com == 'I':
            heapq.heappush(answer, val)
        
    if answer:
        return [heapq.nlargest(1,answer)[0] , heapq.heappop(answer)]
    else:
        return [0,0]
