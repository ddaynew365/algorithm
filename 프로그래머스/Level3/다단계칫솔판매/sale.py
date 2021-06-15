from collections import defaultdict
def solution(enroll, referral, seller, amount):
    answer = []
    graph = dict()
    money = defaultdict(int)
    for i in range(len(enroll)):
        graph[enroll[i]]=referral[i]
    
    for sell in range(len(seller)):
        cur = seller[sell]
        cur_money = amount[sell] * 100
        
        while cur != '-':
            next_money = int(cur_money *0.1)
            
            if next_money < 1:
                money[cur] += cur_money
                break
            
            money[cur] += cur_money - next_money
            cur_money = next_money
            cur = graph[cur]
    
    for i in enroll:
        answer.append(money[i])

    return answer
