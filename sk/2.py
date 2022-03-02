def solution(deposit):
    answer = []
    for depo in deposit:
        if depo > 0:
            answer.append(depo)
        else:
            while depo < 0:
                depo += answer.pop()
            if depo > 0:
                answer.append(depo)
    return answer