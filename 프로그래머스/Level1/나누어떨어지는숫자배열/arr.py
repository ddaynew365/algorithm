def solution(arr, divisor):
    answer = []
    for a in arr:
        if a % divisor == 0:
            answer.append(a)
    if answer:
        answer.sort()
        return answer
    else:
        return [-1]
    
