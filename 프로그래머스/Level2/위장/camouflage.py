"""
이번 문제는 옷의 종류별로 숫자를 구한 후 이를 이용해 연산을 하면 된다고 생각하였다. 따라서 딕셔너리의 키에는 옷의 종류를 값에는 갯수를 넣었다. 

그 후 모든 옷의 종류의 개수에 1을 더해주고 각각 곱해주었다. 이렇게 한 이유는 옷의 종류에 상관없이 무조건 1개만 나오는 경우의 수를 포함한 것이다. 하지만 이 연산은 모든 옷의 종류가
안 나오는 경우를 포함하기 때문에 마지막에 answer 값에 -1을 해주었다.
"""

def solution(clothes):
    dic = {}
    
    for i in clothes:
        kind = i[1]
        if kind in dic:
            dic[kind] = dic[kind] +1
        else:
            dic[kind] = 1
            
    dic_val = dic.values()
    
    dic_val = map(lambda x:x+1,dic_val)
    answer = 1
    for i in dic_val:
        answer = answer * i
    
    answer = answer -1
    return answer
