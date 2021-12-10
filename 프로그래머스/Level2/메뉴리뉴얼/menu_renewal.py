## 나 혼자만의 코드
## 주어진 개수와 order애 따라 모든 조합을 구한 후 원소들을 dict에 저장한다(dict에 저장할 떄 문자열로 바꿔준다) -> dict에서 가장 value가 높은 key들을 answer에 넣고 정렬시킨다
from itertools import combinations
from collections import defaultdict

def perm(order: str, num: int):
    return list(map(sorted,list(combinations(order, num))))
    
def solution(orders, course):
    answer = []
    
    for num in course:
        count = defaultdict(int)
        for order in orders:
            comb = perm(order, num)
            for e in comb:
                e = ''.join(e)
                count[e] += 1
        if count and max(count.values()) > 1:            
            answer += [k for k,v in count.items() if max(count.values()) == v]
    answer = sorted(answer)
    return answer
  


## 다른 사람 코드를 보며 배운 코드
## collections의 Counter 라이브러리와 그 안의 most_common 메소드를 사용하여 개수를 구한다.
from collections import Counter
from itertools import combinations

def solution(orders, course):
    answer = []
    for num in course:
        order_list = []
        for order in orders:
            order_list += combinations(sorted(order), num)
        order_num = Counter(order_list).most_common()
        answer += [k for k,v in order_num if v > 1 and v == order_num[0][1]]
    return sorted(list(map(''.join, answer)))