def solution(s):
    answer = ''
    len_s = len(s)
    locte = len_s // 2
    if len_s % 2 ==0:
        answer += s[locte-1: locte+1]
    else:
        answer += s[locte : locte + 1]
    return answer
