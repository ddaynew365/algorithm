def count(score, area, bonus, score_list):
    score = int(score)
    if area == 'D':
        score = score * score
    elif area == 'T':
        score = score * score * score
    
    if bonus == "*":
        if len(score_list) > 0:
            score_list[-1] *= 2
        score *= 2
    elif bonus == "#":
        score *= -1
    
    score_list.append(score)
    return score_list
    
def solution(dartResult):
    answer = 0
    index = 0
    score_list = []
    while index < len(dartResult):
        score = bonus = ''
        while dartResult[index] not in 'SDT':
            score += dartResult[index]
            index += 1
        area = dartResult[index]
        index += 1
        if index < len(dartResult) and dartResult[index] in "*#":
            bonus = dartResult[index]
            index += 1
        score_list = count(score, area, bonus, score_list)
    answer = sum(score_list)
    return answer