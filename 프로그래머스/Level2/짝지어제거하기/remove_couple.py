def solution(s):
    answer = -1
    stack = []
    
    for i in s:
        stack.append(i)
        
        if len(stack) >= 2 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
    
    if stack:
        answer = 0
    else:
        answer = 1
            

    return answer
