def solution(s):
    answer = []
    slist = []
    alist = []
    
    slist = s.lstrip("{").rstrip("}").split("},{")
    
    for i in slist:
        alist.append(list(map(int, i.split(","))))
    
    alist.sort(key=len)
    
    for i in alist:
        for j in i:
            if j not in answer:
                answer.append(j)
                break
    
    return answer
