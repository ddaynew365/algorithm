def solution(brown, yellow):
    answer = []
    for i in range(1, int(yellow) + 1):
        a = yellow // i
        if yellow % i == 0:
            continue
        else:
            if brown == (a + 2) * (i + 2) - yellow:
                answer = [a + 2, i + 2]
                break
    return answer
