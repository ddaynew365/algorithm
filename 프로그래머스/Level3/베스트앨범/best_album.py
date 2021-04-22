from collections import defaultdict,Counter
import operator
def solution(genres, plays):
    answer = []
    hold = defaultdict(list)
    dic = Counter()
    
    for uni, val in enumerate(zip(genres, plays)):
        hold[val[0]].append((uni,val[1]))
    
    for play_num, play in zip(genres, plays):
        dic[play_num] += play
    
    
    dic_val = sorted(dic.items(),key=operator.itemgetter(1), reverse =True)
    
    for i, wqe in dic_val:
        hold[i].sort(key = operator.itemgetter(1),reverse = True)
        for idx, j in enumerate(hold[i]):
            if idx == 2:
                break
            answer.append(j[0])
        
    return answer
