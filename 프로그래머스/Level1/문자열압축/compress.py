def solution(s):
    answer = 0
    num = len(s)//2 + 1
    answer_list = []
    for i in range(1,num):
        count = 1
        pre = ""
        same = list()
        for j in range(0,len(s),i):
            cur = s[j:j+i]
            if pre == cur:
                count += 1
            else:
                if count == 1:
                    same.append(pre)
                    count =1
                else:
                    same.append(str(count)+pre)
                    count = 1
            pre = cur
            if j+i >= len(s):
                if count == 1:
                    same.append(pre)
                    count =1
                else:
                    same.append(str(count)+pre)
                    count = 1
        answer_list.append(len(''.join(same[1:])))
        answer = min(answer_list)

    if answer == 0:
        answer = 1
    return answer