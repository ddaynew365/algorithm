def solution(record):
    answer = []
    dic_ = {}
    remain = []

    for i in record:
        com = i.split()

        if com[0] == 'Enter':
            dic_[com[1]] = com[2]
            remain.append(com[1])
        elif com[0] == 'Leave':
            remain.remove(com[1])
        else:
            dic_[com[1]] = com[2]


    for i in record:
        com = i.split()

        if com[0] == 'Enter':
            answer.append(dic_[com[1]]+'님이 들어왔습니다.')
        elif com[0] == 'Leave':
            answer.append(dic_[com[1]]+'님이 나갔습니다.')     



    return answer

'''
수정본 -remove에 대한 조건식을 제거, 불필요한 리스트 제거, == 조건 보다 in 조건 비교가 속도가 더 빠르다
'''
def solution(record):
    answer = []
    dic_ = {}

    for i in record:
        com = i.split()

        if com[0] in ['Enter','Change']:
            dic_[com[1]] = com[2]



    for i in record:
        com = i.split()

        if com[0] == 'Enter':
            answer.append(dic_[com[1]]+'님이 들어왔습니다.')
        elif com[0] == 'Leave':
            answer.append(dic_[com[1]]+'님이 나갔습니다.')     



    return answer
