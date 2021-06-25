from collections import deque
s, t = map(int,input().split())

queue =deque()
# 거리, 값, 연산자
start = [0, s, '']
queue.append(start)
flag =False
visited =set()
visited.add(s)

while queue:
    dist, s, opers = queue.popleft()
    if s > int(1e9):
        continue
    if s == t:
        flag = True
        if opers == '':
            print(0)
        else:
            print(opers)
        break

    for oper in ['*', '+', '-', '/']:
        if oper == '*':
            next_value = s*s
        elif oper == '+':
            next_value = s + s
        elif oper == '-':
            next_value = s - s
        else:
            if s != 0:
                next_value = s / s


        if next_value not in visited:
            queue.append([dist + 1, next_value, opers + oper])
            visited.add(next_value)
if flag ==False:
    print(-1)