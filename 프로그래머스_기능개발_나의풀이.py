# 문제 설명
"""
프로그래머스 팀에서는 기능 개선 작업을 수행 중입니다. 각 기능은 진도가 100%일 때 서비스에 반영할 수 있습니다.

또, 각 기능의 개발속도는 모두 다르기 때문에 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고, 이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됩니다.

먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와 각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어질 때 각 배포마다 몇 개의 기능이 배포되는지를 return 하도록 solution 함수를 완성하세요.

제한 사항
작업의 개수(progresses, speeds배열의 길이)는 100개 이하입니다.
작업 진도는 100 미만의 자연수입니다.
작업 속도는 100 이하의 자연수입니다.
배포는 하루에 한 번만 할 수 있으며, 하루의 끝에 이루어진다고 가정합니다. 예를 들어 진도율이 95%인 작업의 개발 속도가 하루에 4%라면 배포는 2일 뒤에 이루어집니다.
"""

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
