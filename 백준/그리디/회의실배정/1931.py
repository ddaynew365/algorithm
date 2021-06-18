"""
해당 문제는 그리디 알고리즘에 관한 문제이다. 그리디 알고리즘에서 가장 중요한 것은 매 순간
올바른 최선의 방법을 선택하는 것이다. 첫 번째 풀이에서 나는 회의 시간이 가장 적은 회의부터
넣는 것이 최선의 방법이라 생각하였지만 반례가 존재하였다. {1-4, 3-5, 4-8}의 경우가 반례 중 하나이다.
두 번째 풀이에서는 끝나는 시간이 가장 빠른 회의부터 차례대로 선택하였다. 이 경우 반례 없이
항상 가장 많은 회의를 선택할 수 있었다.
"""
'''
첫번째 풀이 - 회의 시간이 짧은 것을 기준으로 정함
'''
# import sys
# N = int(sys.stdin.readline().strip())
# con = list()
# answer = list()
# for i in range(N):
#     con.append(list(map(int, sys.stdin.readline().strip().split())))
#
#
# con.sort(key=lambda x: (x[1],x[0]))
# maximum = max([i[1] for i in con])
#
# schedule = (maximum+1) * [False]
#
# for i in con:
#     if i[0] == i[1]:
#         answer.append(i)
#     elif True in schedule[i[0]:i[1]+1]:
#         continue
#     else:
#         schedule[i[0]+1:i[1]] = [True] * (i[1] -i[0]-1)
#         answer.append(i)
# print(len(answer))

'''
두번째 풀이 - 일찍 끝나는 회의를 기준으로 정함
'''
import sys
N = int(sys.stdin.readline().strip())
con = list()

for i in range(N):
    con.append(list(map(int, sys.stdin.readline().strip().split())))


con.sort(key=lambda x: (x[1],x[0]))

count = 0
end = 0
for c in con:
    if end <= c[0]:
        count += 1
        end = c[1]
print(count)



