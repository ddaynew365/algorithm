"""
첫번쨰 풀이 - 주어진 입력 데이터의 범위가 적기 때문에, LRU 알고리즘을 그대로 구현해보았다. 대소문자 구별이 없기 때문에 lower()함수를 사용하여 모두 소문자로 통일하였고
cacheSize가 0인 경우를 대비하여 코드 초반에 0인 경우 단순 계산으로 결과가 나오도록 구현하였다.
"""
from collections import deque

def solution(cacheSize, cities):
    if cacheSize == 0:
        answer = len(cities) * 5
        return answer
    
    answer = 5
    cache = deque([cities.pop(0).lower()])

    for i in cities:
        i = i.lower()
        if i in cache:
            answer += 1
            cache.remove(i)
            cache.append(i)
            continue
        else:
            if len(cache) ==cacheSize:
                cache.popleft()
                cache.append(i)
            else:
                cache.append(i)
            answer += 5

    return answer

"""
deque 함수의 maxlen이라는 매개변수를 알게 되어 코드를 간단화시켰다. 효율성은 위의 코드와 똑같지만 문제를 해결할 때 생각할 부분을 줄일 수 있었다.
"""

from collections import deque

def solution(cacheSize, cities):
    if cacheSize == 0:
        answer = len(cities) * 5
        return answer
    
    answer = 0
    cache = deque(maxlen= cacheSize)

    for i in cities:
        i = i.lower()
        if i in cache:
            answer += 1
            cache.remove(i)
            cache.append(i)
            continue
        else:
            cache.append(i)
            answer += 5

    return answer
