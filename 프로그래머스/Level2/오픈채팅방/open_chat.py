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
