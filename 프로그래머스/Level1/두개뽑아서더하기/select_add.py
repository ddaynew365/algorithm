def solution(numbers):
    answer = []
    n = len(numbers)
    for i in range(n):
        for j in range(i+1,n):
            answer.append(numbers[i]+numbers[j])
    answer = list(set(answer))
    answer.sort()
    return answer
