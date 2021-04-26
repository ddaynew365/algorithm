"""
해당 문제를 쉽게 풀기 위해서는 수리 능력이 필요했다. 나는 노란 카펫의 타일 개수로 만들 수 있는 모든 직사각형을 고려하여 각각의 경우마다 갈색 타일의 개수를 계산하여 주어진 갈색타일 개수와
비교하는 방법을 사용하였다. 다른 사람들의 풀이를 분석한 결과 역시 나와 비슷하게 수리적인 방법을 사용한 것을 볼 수 있었다.
"""
def solution(brown, yellow):
    answer = []
    for i in range(1, yellow+1):
        a = yellow // i
        rest = yellow % i
        if rest != 0:
            continue
        else:
            if brown == (a+2) * (i+2) - yellow:
                answer = [a+2, i+2]
                break
    return answer
