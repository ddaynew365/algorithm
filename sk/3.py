from collections import defaultdict
def full_navi(num, limit, cur_price, prices):
    if limit == -1:
        return cur_price
    return full_navi(num, limit-1, min(cur_price, limit * prices[1] + 2 * (num-limit) * prices[0]), prices)

def solution(color, prices):
    answer = 0
    color_kinds = ['B', 'W', 'R', 'Y', 'G']
    tops, pants = defaultdict(int), defaultdict(int)
    remain_pairs= 0
    remain_tops, remain_pants = [], []
    for c in color:
        tops[c[0]] += 1
        pants[c[1]] += 1
    
    for c in color_kinds:
        dup_num = min(tops[c], pants[c])
        tops[c] -= dup_num
        pants[c] -= dup_num
        if tops[c] > 0:
            remain_pairs += tops[c]
            remain_tops.append(tops[c])
        if pants[c] > 0:
            remain_pants.append(pants[c])
        answer += (dup_num * prices[0])

    result = full_navi(remain_pairs, remain_pairs, int(1e9), prices)
    answer += result
    return answer
