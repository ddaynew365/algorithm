def solution(t, m):
    answer = 0
    new_t = sorted(t)
    for i in range(m):
        answer += (new_t[i] + 1)
    return answer