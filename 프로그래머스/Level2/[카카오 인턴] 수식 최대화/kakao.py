from itertools import permutations
def solution(expression):
    answer = 0
    cur_num = ''
    num_list= list()
    as_list = list()
    as_map = dict()
    for char in expression:
        if char.isdigit():
            cur_num += char
        else:
            as_list.append(char)
            num_list.append(int(cur_num))
            cur_num = ''
    num_list.append(int(cur_num))
    as_set = list(set(as_list))
    perm = list(permutations(as_set, len(as_set)))
    candi = []
    for ranks in perm:
        num = num_list[:]
        asl = as_list[:]
        for i in ranks:
            while i in asl:
                idx = asl.index(i)
                asl.pop(idx)
                if i == "*":
                    num[idx + 1] = num[idx] * num[idx + 1]
                elif i == "+":
                    num[idx + 1] = num[idx] + num[idx + 1]
                elif i == "-":
                    num[idx + 1] = num[idx] - num[idx + 1]
                num.pop(idx)
        if num[0] > 0:
            candi.append(num[0])
        else:
            candi.append(-1 * num[0])
    return max(candi)