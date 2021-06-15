def check(start,logs):
    start =start
    end = start + 999
    count = 0
    for s,e in logs:
        if e >= start and s <= end:
            count += 1
    return count

def solution(lines):
    answer = 1
    cur_time = []
    logs= []
    # 데이터 전처리- 모든 시간을 초로 환산하여 수로 표현
    for i in lines:
        y,a,t = i.split()
        a = a.split(':')
        time = int(a[0]) * 3600 + int(a[1]) * 60 + float(a[2])
        end = int(time*1000)
        t = int(float(t.replace('s',''))*1000)
        start = end - t +1
        if start < 0:
            start = 0
        log = [start,end]
        logs.append(log)
    # 각 요청의 요청 시간과 완료시간을 check함수에 넣어 해당 기간안에 다른 요청이 몇개나 들어왔는지 확인
    for j in logs:
        
        answer = max(answer,check(j[0],logs),check(j[1],logs))
        
        
    return answer
