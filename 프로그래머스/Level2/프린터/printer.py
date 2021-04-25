"""
이번 문제는 큐를 사용하는 것이 유용하다고 생각하여 deque 자료구조를 사용하였다. 처음에 풀었을 때, 빼냈다가 다시 집어 넣은 데이터의 인덱스를 어떻게 저장해야 하는지 생각하는 부분이
많은 어려움을 겪었다. 그러다가 나머지 연산과 조건식을 사용하여 풀어냈지만 많은 아슁움을 남겼다. 그 후 다른 사람의 풀이를 참고한 결과 any() 함수의 사용방법과 이차원 리스트를 사용하면
수월하게 해결할 수 있다는 것을 알게 되었다. 최근 딕셔너리 자료형을 공부하면서 이차원 리스트를 생각하는 것에 유연하지 못하였다고 생각한다.
결국 다른 사람의 풀이에 deque를 적용하여 효율성이 제일 빠른 코드를 완성하였다.
"""

# 처음 푼 형식
#==============================================================================================================================================================================
from collections import deque

def solution(priorities, location):
    p = deque(priorities)
    lank = [0] * len(priorities)
    x = 1
    i = 0
    
    
    while p:
        while lank[i] != 0:
            i += 1
            i = i % len(priorities)
        # 맨 앞 값 꺼내기
        v = p.popleft()
        # p가 비어있지 않고 꺼낸값이 우선순위 1등이 아니라면 다시 넣기
        if p and v < max(p):
            p.append(v)
        # p가 비어있거나 꺼낸 값이 우선순위 1등이라면 인쇄
        else:
            lank[i] = x
            x +=1   
        i += 1
        i = i % len(priorities)
        
    answer = lank[location]
    return answer
  
# 다른 사람의 풀이
#==============================================================================================================================================================================
def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer
              
              
# 위의 풀이의 장점을 deque에 적용시킨 풀이
#==============================================================================================================================================================================
from collections import deque

def solution(priorities, location):
    queue = deque()
    lank= [0] * len(priorities)
    x =1
    
    for i,v in enumerate(priorities):
        queue.append([i,v])
    
    while queue:
        cur = queue.popleft()
        if any(cur[1] < p[1] for p in queue):
            queue.append(cur)
        else:
            if cur[0] == location:
                return x
            x+=1
