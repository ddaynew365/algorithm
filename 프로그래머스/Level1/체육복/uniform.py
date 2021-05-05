def solution(n, lost, reserve):
    answer = 0
    non = 0
    # lost와 reserve에서 중복되는 학생은 제외
    new_lost = list(set(lost) - set(reserve))
    new_reserve = list(set(reserve) - set(lost))

    # pop()함수로 lost 리스트 중 번호가 높은 학생부터 먼저 빼내어 뒷번호 부터 확인
    for i in range(len(new_lost)):
        v = new_lost.pop()
        if v + 1 in new_reserve:
            new_reserve.remove(v+1)
        elif v in new_reserve:
            new_reserve.remove(v)
        elif v -1 in new_reserve:
            new_reserve.remove(v-1)
        else:
            non+=1
            
    # 전체 학생 중 도난당하고 빌릴수도 없는 학생 수 빼기
    answer = n - non
        
    return answer
