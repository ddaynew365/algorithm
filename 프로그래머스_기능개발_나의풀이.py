# 풀이 과정
"""
현재 나는 코딩테스트를 준비하면서 파이썬과 알고리즘 공부를 병행 중이다. enumerate() 함수를 사용하니 for문을 다룰 때 상당히 편안함을 느꼈다. 또한 학교를 다니면서 분명 알고리즘으로
풀 수 있는 방법인데 그 알고리즘이 무엇인지 생각이 나지 않아 직접 구현한 부분도 있었다.
먼저 progresses 리스트와 speeds리스트를 사용하여 남은 날이 각각 몇일인지를 구해놓고 이를 remain_days 리스트에 담아 놓았다. 
그 후 첫 번째 기능이 베포될때마다 그 뒤의 기능들이 완성되었는지를 비교하여 동시에 베포되는 기능의 수를 세는 방식으로 풀었다. 결과적으로 문제는 풀었지만 어떠한 알고리즘을 썼다면
더욱 좋은 코드를 만들었을텐데 그러지 못해 아쉬웠다.
"""
import math

def solution(progresses, speeds):
    answer = []
    remain_days = []
    cur = 0
    
    for i,prog in enumerate(progresses):
        remain_prog = 100 - prog
        remain_day = remain_prog / speeds[i]
        remain_day = math.ceil(remain_day)
        remain_days.append(remain_day)
        
    
    for i, a in enumerate(remain_days):
        release_num =0
        if cur > i:
            continue
        for j, b in enumerate(remain_days):
            if cur > j:
                continue
            if a >= b:
                release_num+=1
                continue
            else:
                break
        answer.append(release_num)
        cur =cur+release_num


        
    return answer
