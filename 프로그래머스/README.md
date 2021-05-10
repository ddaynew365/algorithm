## 파이썬 문법 정리
1. from collections import deque


2. from collecrions import defaultdict


4. import heapq


5. 람다식
- 예시) list(map(lambda x: x ** 2, range(5)))
- 익명함수로 왼쪽은 매개변수 오른쪽은 반환되는 형태를 의미
- map(함수, 리스트)로 리스트의 원소들을 하나씩 꺼낸 후 함수를 적용하여 다시 리스트에 집어넣는 함수다

6. 리스트.startswith() / 리스트.endswith()
- 문자열의 시작과 끝 부분이 괄호 안과 일치하는지에 따라 bool값을 반환하는 함수

7. sort(key='',reverse='')
- 리스트 정렬 함수
- key는 정렬 기준을 입력할 수 있다
- reverse는 내림차순이 되게 한다

8. ''.join(리스트)
- 문자열 리스트를 하나의 문자열로 합치는 기능

9. all('iterable') / any('iterable')
- all(): 인자로 받은 데이터의 모든 요소가 True일때만 True, 요소가 비어있으면 True
- any(): 인자로 받은 요소 중 하나라도 True면 True, 요소가 비어있으면 False


## 자료구조 정리
1. 큐

2. 스택

3. 해시

4. 힙

## 알고리즘 정리
1. 이진탐색
2. dfs
3. bfs
4. 완전탐색
5. 그리드 알고리즘
6. 다이나믹 프로그래밍
7. 다익스트라 알고리즘
