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
