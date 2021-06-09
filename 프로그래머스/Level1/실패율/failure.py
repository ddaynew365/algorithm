from collections import Counter
def solution(N, stages):
    answer = []
    suc = [0] * (N+1)
    # 스테이지별 머무르고 있는 도전자수 
    remain = dict(Counter(stages))
    for i in range(N+1):
        if i in remain:
            suc[i] = remain[i]

    total = len(stages)
    fail = dict()
    for i in range(1,N+1):
        if total == 0:
            fail[i] = 0
            continue
        fail[i] = suc[i]/total
        total -= suc[i]

    print(fail)
    
    
    answer = sorted(fail, key = lambda x:fail[x], reverse =True)

    return answer
