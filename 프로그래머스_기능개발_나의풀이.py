
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
        
    print(remain_days)
    
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
