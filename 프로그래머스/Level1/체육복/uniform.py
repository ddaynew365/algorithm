"""
해당 문제는 우선 도난당하면서 체육복을 두개 가져온 학생들을 처리해주는 것이 중요하다. 이런한 경우 도난당하지도 체육복을 두 개 가져오지도 않은 학생과 똑같이 처음부터 1개를 가지고 있다고
생각하면 편하기 때문에 2개의 리스트에서 서로 겹치는 학새들은 모두 제외하였다. 그 후 도난당한 학생 중 가장 높은 학번부터 차례차레 꺼내서 뒷번호부터 비교하여 체육복을 빌릴 수 있는지에 
대해 확인하였다.
이 때 순서를 왜 이렇게 하냐면 체육복을 2개 가져온 학생의 앞번호 뒷번호 모두가 도난당했으면 어디를 선택하느냐에 따라 값이 달라질 수 있기 떄문에 끝에서부터 뒷번호를 비교하여
이를 방지하였다
"""
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
