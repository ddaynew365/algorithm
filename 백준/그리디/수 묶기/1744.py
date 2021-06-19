import sys
# 데이터 입력
N = int(sys.stdin.readline().strip())
array = list()
for i in range(N):
    array.append(int(sys.stdin.readline().strip()))
# 정렬 및 음수 양수 나누기
array.sort()
minus = [i for i in array if i<=0]
plus = [i for i in array if i > 0]

cur = 1
# 곱셈 후에 음수 리스트
afterminus = []

if len(minus) < 2:
   sum_mi = sum(minus)
else:
    for i,val in enumerate(minus):
        if i == 0:
            cur *= val
        elif i % 2 == 1 or i ==len(minus)-1:
            cur *= val
            afterminus.append(cur)
            cur = 1
        elif i % 2 == 0:
            cur *= val
    sum_mi =sum(afterminus)

# 곱셈 후에 양수리스트
afterplus =[]

if len(plus) < 2:
    sum_pl = sum(plus)
else:
    for i,val in enumerate(reversed(plus)):
        if val == 1:
            if cur != 1:
                afterplus.append(cur)
                cur = 1
            afterplus.append(val)
        elif i % 2 ==1 or i ==len(plus) -1:
            cur *= val
            afterplus.append(cur)
            cur = 1
        elif i % 2 ==0:
            cur *= val

    sum_pl = sum(afterplus)

print(sum_pl + sum_mi)





