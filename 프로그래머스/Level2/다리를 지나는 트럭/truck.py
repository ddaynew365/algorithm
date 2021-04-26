"""
지난번에 실패했던 문제인 '다리를 지나는 트럭'을 다시 한번 풀어보았다. 파이썬의 여러 라이브러리 함수를 배웠고 queue 자료구조를 사용하여 문제를 시뮬레이션으로 풀어냈다.
"""

from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0

    on_truck = deque()
    wait_truck =deque([[val,bridge_length ] for  val in truck_weights])

    while on_truck or wait_truck:
        
        time += 1
        
        for i in on_truck:
            i[1] -= 1
            
        if on_truck and on_truck[0][1] == 0:
             on_truck.popleft() 
                
        if wait_truck and sum([i[0] for i in on_truck])+wait_truck[0][0] <= weight:
            c = wait_truck.popleft()
            on_truck.append(c)    
              
    return time
