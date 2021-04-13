/*
프로그래머스 - 완주하지 못한 선수
*/
#초기 코드

def solution(participant, completion):
    com = sorted(completion)
    parti = sorted(participant)
    for i in com:
        if i in parti:
            parti.remove(i)


    answer = parti[0]
    return answer
  
/*
결과는
  정확성: 50
  효율성: 10
   
  확인 결과 효율성이 너무 부족하였다. 어디를 고쳐야 효율성이 좋아질지 찾아봐야겠다
 */
