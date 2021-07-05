# 딕셔너리와 리스트 사용, 다시
from collections import defaultdict
import heapq, sys

def get_pic_frame():
    res = 0
    min_like = 1000
    old_when = 1000
    for idx, val in enumerate(pic_frame):
        if val == 0:
            return idx

    for j in pic_frame:
        tmp_like = cand_like[j]
        tmp_when = cand_when[j]
        if tmp_like < min_like:
            min_like = tmp_like
            old_when = tmp_when
            res = j
        elif tmp_like == min_like and tmp_when < old_when:
            min_like = tmp_like
            old_when = tmp_when
            res = j
    return res
n = int(input()) # 사진틀의 개수
num_cc = int(input()) # 추천 갯수
ord_cc = list(map(int,input().split())) # 추천 순서
pic_frame = [0] * 20 # 사진틀(자료구조)
cand_like = [0] * (101) #후보 추천 횟수
cand_where = [-1] * (101) # 후보가 어떤 사진틀에 걸려있는 지
cand_when = [-1] * 101

for i, cur in enumerate(ord_cc):
    # 후보가 사진틀에 올라가 있을까
    if cand_where[cur] != -1:
        cand_like[0] += 1
    else:
        # 비어있는 또는 후보를 넣을 사진틀을 얻는다.
        pos = get_pic_frame()
        delete_cand = pic_frame[pos]
        # delete_cand는 사진틀에서 내리면서, 좋아요도 초기화한다
        if delete_cand != 0:
            cand_where[delete_cand] = -1
            cand_like[delete_cand] = 0
        cand_where[cur] = pos
        cand_like[cur] = 1
        cand_when[cur] = i
        pic_frame[pos] = cur

for i in range(1, 100):
    print(cand_where)
    if cand_where[i] != -1:
        print(i,end=' ')
