# 실패 다시 도전
import sys
N = int(sys.stdin.readline().strip())
con = list()
answer = list()
for i in range(N):
    con.append(list(map(int, sys.stdin.readline().strip().split())))


con.sort(key=lambda x: (x[1],x[0]))
maximum = max([i[1] for i in con])

schedule = (maximum+1) * [False]

for i in con:
    if i[0] == i[1]:
        answer.append(i)
    elif True in schedule[i[0]:i[1]+1]:
        continue
    else:
        schedule[i[0]+1:i[1]] = [True] * (i[1] -i[0]-1)
        answer.append(i)
print(len(answer))

