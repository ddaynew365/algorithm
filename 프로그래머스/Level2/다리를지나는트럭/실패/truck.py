"""
이번 문제를 풀면서 나의 약점을 알게 되었다. 코드 구상 단계에서 제대로 생각하지 않고 구현을 하는 것이었다. 처음에는 시뮬레이션 형식으로 코드를 짜다가 중간에 경우의 수마다 시간을
더하는 방식으로 생각을 바꾸면서 2가지 방법이 서로 꼬여 이도 저도 아닌 코드가 되었다. 알고리즘을 좀 더 익히게 되고 코딩 실력이 늘면 다시 한번 도전해볼 생각이다.
"""
def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_on_bridge =[]
    timer= []
    
    for i, cur_truck in enumerate(truck_weights):
        
        while True:
# 맨 처음
            if answer == 0:
                truck_on_bridge.append(cur_truck)
                timer.append(bridge_length)
                truck_weights.pop(i)
                answer = answer + 1
                break
# 새로 들어올 수 있는 트럭 존재
            elif (sum(truck_on_bridge[0])+cur_truck) <= weight: 
                answer = answer + 1
                for time in timer:
                    time = time-1

                if timer[0] == 0:
                    truck_on_bridge.pop(0)

                truck_on_bridge.append(cur_truck)
                timer.append(bridge_length)
                truck_weights.pop(i)
                break
# 들어올 수 있는 트럭이 없을 때
            else: 
                answer = answer + 1
                for time in timer:
                    time = time-1

                if timer[0] == 0:
                    truck_on_bridge.pop(0)
                                
    return answer
