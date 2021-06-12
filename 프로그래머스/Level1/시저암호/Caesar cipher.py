def solution(s, n):
    answer = ''
    for i in range(len(s)):
        new_s = ord(s[i]) + n
        if s[i] == ' ':
            answer += ' '
            continue
        elif ord(s[i]) < 97 and new_s > 90:
            new_s= new_s - 26
        elif new_s > 122:
            new_s = new_s - 26
            
        answer += chr(new_s)

    return answer
