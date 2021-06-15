'''
프로그래머스 - 완주하지 못한 선수
'''
#초기 코드

# def solution(participant, completion):
#     com = sorted(completion)
#     parti = sorted(participant)
#     for i in com:
#         if i in parti:
#             parti.remove(i)


#     answer = parti[0]
#     return answer
 
'''
결과는
  정확성: 50
  효율성: 10
   
  확인 결과 효율성이 너무 부족하였다. 어디를 고쳐야 효율성이 좋아질지 찾아봐야겠다
'''

# 두번쨰 풀이 - 이중 for문이 문제였다. 정렬도 꽤 큰 연산이지만 주어진 입렵값의 조건에 의하면 충분히 통과할 수 있었다. 하지만 나는 해시테이블 방식을 적용하여 문제를 해결하였다.
# 전체 선수의 수를 이름별로 센 후 완주한 선수들은 1씩 빼주었다. 그렇게 되면 완주한 선수들은 결국 해시 결과값이 0이 될 것이고 완주하지 못한 선수는 결과값이 1이 될 것이다.

from collections import defaultdict

def solution(participant, completion):
    answer = ''
    a= defaultdict(int)
    for i in participant:
        a[i]+= 1
    
    for j in completion:
        if j in a:
            a[j] -= 1
    
    for i in a.items():
        if i[1] == 1:
            answer = i[0]
            break
    
    return answer
