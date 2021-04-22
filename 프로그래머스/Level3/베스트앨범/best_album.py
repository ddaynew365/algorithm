"""
이번 문제는 파이썬안에 있는 모듈들을 사용해보았다. collecions모듈안에 defaultdict함수는 딕셔너리에서 하나의 키에 여러개의 값을 넣기 위해 사용하였고 Counter함수는 딕셔너리에 하나의 키에 
대해서 값을 넣을 떄 그 키가 몇번 등장하였는지 개수를 세거나 값을 더하기 위해 사용하는 함수였다. 또한 operator.itemgetter()은 딕셔너리의 value를 기준으로 정렬하기 위해서 사용하였다.

우선 각 장르별로 재생횟수를 모두 더해 큰 순서대로 정렬을 하였다. 또한 장르를 키로 잡고 [ 고유번호, 재생횟수]를 값으로 넣은 딕셔너리를 만들고 이 역시 큰 순서대로 정렬을 시켰다.

그후 이중 for문을 사용하여 재생횟수가 많은 순서대로 장르를 불러와 그 안에서 재생횟수가 많은 2개의 노래의 고유번호를 answer리스트에 차례대로 넣어주었다.
"""
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
