"""
이번 문제는 heapq라이브러리를 사용하여 문제를 풀어냈다. heapq라이브러리는 자료구조 heap을 구현한 것으로 해당 문제의 경우 heap으로 풀지 않으면 효율성 부분에서 좋은 점수를 받기
힘들다. 나는 heapq 라이브러리를 사용하고도 처음에 효율성 분야에서 0점을 받았다. 여러가지 코드를 수정하며 건드린 결과 min(scoville)이 문제였다. min()함수는 시간 복잡도가
O(n)을 가지는데 반해 heapq라이브러리를 사용한 scoville[0]은 O(1)밖에 들지 않기 떄문이다.
"""
import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville[0]< K :
        if len(scoville) < 2:
            answer = -1
            break
        safe1 = heapq.heappop(scoville)
        safe2 = heapq.heappop(scoville)
        heapq.heappush(scoville, safe1 + 2 * safe2)
        answer += 1

        
    return answer
