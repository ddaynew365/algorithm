def solution(user_id, banned_id):
    answer = 0
    all_candi_id = list()
    for ban in banned_id:
        candi_id = list()
        for user in user_id:
            if len(user) != len(ban):
                continue
            is_candi = True
            for i in range(len(user)):
                if user[i] != ban[i] and ban[i] != '*':
                    is_candi = False
                    break
            if is_candi:
                candi_id.append(user)
        
        all_candi_id.append(candi_id)
    answer = list()
    
    def combination(candi_list, cur, length):
        if cur and len(cur) == length:
            cur.sort()
            if cur not in answer:
                answer.append(cur)
            return
        candi = candi_list[0]
        if not candi:
            return
        for i in candi:
            if i in cur:
                continue
            combination(candi_list[1:], cur + [i] ,length)
            
    combination(all_candi_id, [], len(all_candi_id))
    
    return len(answer)
  