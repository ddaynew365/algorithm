import sys
from collections import defaultdict
from itertools import combinations
# 입력을 받는다
n, k = map(int, sys.stdin.readline().strip().strip().split())
arr = []
for _ in range(n):
    arr.append(sys.stdin.readline().strip())


# 지민은 꼭 5개는 알려줘야함 : a n t i c
# k개를 알려줄 수 있다고 치면, 실제로는 k-5개만큼은 자유롭게 선택이 가능
# 경우의 수를 한번 살펴본다...
# 예) k = 7 ----> a n t i c를 빼고 나머지 2개로 기회를 만들 수 있다
    # b d
    # b e
    # b f
    # b g
    # ....
    # y z
    # 26 - 5 = 21 개 중에서 2개를 고르는 경우의 수
    # ---> 21C5 ---> 210 ??
# 선택하는 알파벳을 고른 다음에 실제로 주어진 단어를 읽을 수 있는지 확인해봄
# 어떻게???
    # a n t i c .... b d 라고 하면
    # a n t a rctica 실패
    # a n t a hellotica 실패
    # a n t a c a rtica 실패 ---> 0개의 단어를 읽었다...
        # 위와 같은 흐름을 모두 돌린다
max = -1
if k >= 5:
    remain_alpha = set()
    for a in arr:
        remain_alpha.update(set(a) - {'a', 'n', 't', 'i', 'c'})

    for c in combinations(remain_alpha, k-5):
        count = 0
        for a in arr:
            result = set(a) - {'a', 'n', 't', 'i', 'c'} - set(c)
            if result == set():
                count += 1
        if count > max:
            max = count
    print(max)

# 만약에 입력이 k가 5보다 작으면 ??? 무조건 0...
else:
    print(0)

