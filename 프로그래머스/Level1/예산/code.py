def solution(d, budget):
    answer = 0
    sum_ = 0
    d.sort()
    for i in d:
        if sum_ + i > budget:
            break
        sum_ += i
        answer += 1
    return answer
