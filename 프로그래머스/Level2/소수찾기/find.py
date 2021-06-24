"""
해당 문제는 순열을 사용해서 모든 경우의 수를 탐색해야 하는 유형이었다. 이번 기회를 통해 순열을 구하는 알고리즘에 대해 배웠다.
순열 알고리즘은 dfs를 사용한 방식으로 재귀함수를 사용한다. 또한 평소 소수를 찾는 문제는 에라토스테네스의 채를 사용하였다. 물론 이 문제 역시
에라토스테네스의 채를 사용하였지만 그 방식이 좀 달랐다. 이전에는 경우의 수 중 가장 큰 수까지 리스트를 만들어서 미리 소수를 다 구하는 방식을
사용하였는데 그렇게 되면 시간 복잡도가 너무 커져 문제가 해결되지 않았다. 따라서, 순열로 나온 수들을 하나씩 소수를 판별하는 알고리즘으로 구현했다.
그 결과, 미리 소수를 모두 구하는 방법보다 매우 빠른 속도로 문제가 해결되었다.
"""
def solution(numbers):
    num_list = sorted(numbers, reverse=True)
    def isdecimal(i):
        if i == 1 or i ==0:
            return False
        for j in range(2, int(i ** (1 / 2))+1):
            if i % j == 0:
                return False
        return True
    # 모든 조합
    pre_element = []
    result = []

    def dfs(element):
        if len(pre_element) != 0:
            a = int(''.join(pre_element[:]))
            if a not in result:
                result.append(a)

        for e in element:
            next_element = element[:]
            next_element.remove(e)

            pre_element.append(e)
            dfs(next_element)
            pre_element.pop()

    dfs(num_list)

    count = 0
    for i in result:
        if isdecimal(i):
            count += 1
    return count

'''
아래 식은 파이썬틱한 풀이법으로 itertools 모듈의 permutaions를 사용하여 풀어냈다.
'''
from itertools import permutations
import math

def check(n):
    k = math.sqrt(n)
    if n < 2:
        return False

    for i in range(2, int(k)+1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = []
    for k in range(1, len(numbers)+1):
        perlist = list(map(''.join, permutations(list(numbers), k)))
        for i in list(set(perlist)):
            if check(int(i)):
                answer.append(int(i))

    answer = len(set(answer))

    return answer
