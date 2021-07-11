import sys
sudoku = []

# 입력을 받음
for _ in range(9):
    sudoku.append(list(map(int,sys.stdin.readline().strip().split())))
arr = list(range(1,10))

# 빈 공간들 좌표를 모은다.
empty_space = []
for y in range(9):
    for x in range(9):
        if sudoku[y][x] == 0:
            empty_space.append([y,x])
n = len(empty_space)

# 함수
def bt(pos):

    # final condition
        # 출력하고 끝냄
    if pos == n:
        for an in sudoku:
            for char in an:
                print(char ,end =' ')
            print()
        return

    # 언제 채울 수 있냐면
    # 1. empty_space가 있는 작은 사각형에 숫자가 중복이 안될 떄! -> 그 작은 사각형을 어떻게 판단할지
    # 2. empty_space가 있느 새로줄에 숫자가 중복이 안될 떄! -> 세로줄을 어떻게 판단할지
    # 3. empty_space가 있는 가로줄에 숫자가 중복이 안될 때 -> 가로줄을 어떻게 판단할지
    y, x = empty_space[pos]
    sy, sx = y//3 + 1, x//3 +1
    l = [ sudoku[j][i] for i in range(((sx-1)*3), sx*3) for j in range(((sy-1)*3), sy*3)]

    for i in arr:
        if i not in sudoku[y] and i not in [li[x] for li in sudoku] and i not in l:
            sudoku[y][x] = i
            bt(pos+1)
            sudoku[y][x] = 0


bt(0)






#
# bt(empty_space[0],sudoku)
#


# 백 트래킹
#메인
    # 어떻게 채우지?
        # 입력을 받은 다음에
        # 빈 공간들 좌표를 모은다. (y, x) --> empty_space

        # 모든 empty_space를 어떤 값으로 다 채웠다고 판단하면 그 상태가 정답이므로 출력을 한다.

# 함수
    # final condition
        # 출력하고 끝냄

    # 앞으로 할 일은 empty_space를 0~9로 채워보는 건데
    # 언제 채울 수 있냐면
        # 1. empty_space가 있는 작은 사각형에 숫자가 중복이 안될 떄! -> 그 작은 사각형을 어떻게 판단할지
        # 2. empty_space가 있느 ㄴ새로줄에 숫자가 중복이 안될 떄! -> 세로줄을 어떻게 판단할지
        # 3. empty_space가 있는 가로줄에 숫자가 중복이 안될 때 -> 가로줄을 어떻게 판단할지
    # 1, 2, 3이 만족이 되면 일단 '그 숫자'로 채워보고

    # recur(pos+1)
        # 만약에 정답을 찾았으면 끝내는 방향으로 가고
        # 못 찾았으면 다른 숫자로 채워보고

    # 마저 진행을 해본다...
