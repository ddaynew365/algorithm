from collections import  defaultdict
def solution(n, t, m, timetable):
    answer = ''
    start = 540    
    ntt, bus = list(), list()
    btw = defaultdict(list)
    timetable.sort()
    # 시간: 문자열에서 숫자로
    for p in timetable:
        hour, minute  = map(int,p.split(":"))
        ntt.append(hour* 60 + minute)
    # 버스 오는 시간 리스트 생성
    for i in range(n):
        bus.append(start + i*t)
    # 사람마다 어느 시간 버스에 타는지 계산
    for p in ntt:
        for i in range(n):
            if p <= bus[i] and len(btw[bus[i]]) < m:
                btw[bus[i]].append(p)
                break
    # 마지막 시간 버스의 대기열이 m보다 작으면 마지막 버스 시간이 정담
    if len(btw[bus[-1]]) < m :
        result= bus[-1]
    # 마지막 시간 버스의 대기열이 꽉 찼으면 마지막에 있는 사람 -1분이 정답
    else:
        result = btw[bus[-1]][-1] - 1
    
    hour, minute = result// 60, result %60
    answer = str(hour).zfill(2) + ":" + str(minute).zfill(2)
    return answer