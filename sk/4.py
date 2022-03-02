from collections import defaultdict
def solution(rsp3):
    rsp_rule= {'RS':'R', 'SR': 'R', 'SP':'S', 'PS':'S','RP':'P', 'PR':'P'}
    p_score = [0, 0, 0]
    for r in rsp3:
        round_num = defaultdict(int)
        p = [char for char in r]
        round_num[p[0]] += 1
        round_num[p[1]] += 1
        round_num[p[2]] += 1
        if round_num['R'] > 0 and round_num['P'] > 0 and round_num['S'] >0:
            continue
        if round_num['R'] == 3 or round_num['P'] == 3 and round_num['S'] == 3:
            continue
        round_result = ''
        for char in round_num:
            if round_num[char] != 0:
                round_result += char
        winner_char = rsp_rule[round_result]
        winner_list = list()
        for idx, char in enumerate(p):
            if char == winner_char:
                winner_list.append(idx)
        if len(winner_list) == 1:
            p_score[winner_list[0]] += 2
        else:
            if p_score[winner_list[0]] > p_score[winner_list[1]]:
                p_score[winner_list[1]] += 2
            elif p_score[winner_list[0]] < p_score[winner_list[1]]:
                p_score[winner_list[0]] += 2
            else:
                p_score[winner_list[0]] += 1
                p_score[winner_list[1]] += 1
    return p_score