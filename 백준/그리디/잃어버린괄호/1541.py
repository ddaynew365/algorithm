"""
해당 문제는 그리디 알고리즘 관련 문제이지만 실제로는 문자열 처리에 중점이 더 있는 문제였다. 식에
'-'가 등장하는 순간 그 뒤 수들을 모두 더해 '-'등장 이전 수들의 합에서 빼주기만 하면 되기 떄문이다.
좀 더 편하게 알고리즘을 수행하기 위해 문자열로 된 식을 숫자마다 리스트에 집어 넣었고 +는 생략, 첫
번째 -만 리스트에 넣어주었다.
"""
import sys
equation = sys.stdin.readline().strip()
curnum = ''
equ_list =[]
flag =True
# 입력값 전처리
for i in equation:
    if i == '-' or i == '+':
        equ_list.append(int(curnum))
        curnum = ''
        if i == '-' and flag:
            equ_list.append(i)
            flag =False
    else:
        curnum += i
equ_list.append(int(curnum))
# 알고리즘 수행
ans = 0
sub = 0
for i,val in enumerate(equ_list):
    if val =='-':
        sub = sum(equ_list[i+1:])
        break
    ans += val
ans = ans - sub
print(ans)