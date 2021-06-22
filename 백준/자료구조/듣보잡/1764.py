"""
해쉬맵인 딕셔너리를 사용하여 키에는 사람의 이름 값에는 해당하는 집합의 개수를 넣어주었다.
그리고 값이 2인 경우의 사람들만 사전순으로 정렬하여 문제를 해결하였다.
"""
import sys
from collections import defaultdict
N, M = map(int,sys.stdin.readline().split())

no_wls = defaultdict(int)

for _ in range(N):
    no_wls[sys.stdin.readline().strip()] += 1
for _ in range(M):
    no_wls[sys.stdin.readline().strip()] += 1
answer = []
for key , value in no_wls.items():
    if value == 2:
        answer.append(key)
answer.sort()
print(len(answer))
for i in answer:
    print(i)
