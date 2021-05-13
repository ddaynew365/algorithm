"""
첫번째 도전 실패
"""
import heapq


def solution(jobs):
    answer = 0
    ready_queue = []
    time = 0
    work = 0
    visit = []
    for i in jobs:
        i[0], i[1] = i[1], i[0]
    for _ in range(1000):

        for i in jobs[:]:
            if i[1] <= time and i not in visit and i not in ready_queue:
                heapq.heappush(ready_queue, i)
        if len(visit) == len(jobs):
            break

        if ready_queue:
            work = heapq.heappop(ready_queue)
            visit.append(work)
            answer += (time - work[1])
            time += work[0]
        else:
            time += 1

    return answer

"""
두번째 도전 후 성공 -> 문제에 명시된 조건을 제대로 보지 못하여서 결과값을 만드는 계산식에 오류가 있었다. 하지만 시간 복잡도가 너무 크다. 아마 매 반복마다 조건식이 너무 많고 
시뮬레이션 형식이기 때문인 것 같다. 다음번에 풀 때는 이러한 부분을 수정하여 시간 복잡도를 줄이려고 해보겠다.
"""
import heapq


def solution(jobs):
    answer = 0
    ready_queue = []
    time = 0
    finish = []
    
    for i in jobs:
        i[0], i[1] = i[1], i[0]
        
        
    while len(finish) < len(jobs):
        # 요청시간이 현재 시간보다 적은 job을 준비 큐에 넣기
        for i in jobs:
            if i[1] <= time and i not in finish and i not in ready_queue:
                heapq.heappush(ready_queue, i)
        # 준비 큐에 job이 있다면 처리시간이 가장 짧은 job을 꺼내 일을 시킴
        if ready_queue:
            work = heapq.heappop(ready_queue)
            finish.append(work)
            time += work[0]
            answer += (time - work[1])

        # 준비 큐에 job이 없다면 시간을 1초 증가
        else:
            time += 1
    # 평균 시간       
    answer //= len(jobs)
    return answer


