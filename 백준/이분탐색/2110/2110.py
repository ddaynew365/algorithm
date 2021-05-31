import sys
# 임의의 길이가 주어졌을 때, 배치 가능한 공유기의 수를 반환하는 함수
def count(m, loc):
    cnt = 1
    curr = loc[0]
    for i in range(1, len(loc)):
        if curr + m <= loc[i]:
            cnt += 1
            curr = loc[i]
    return cnt

# 사용자의 입력을 받는 코드
n, c = map(int, sys.stdin.readline().split())
locate = [int(sys.stdin.readline()) for _ in range(n)]
# 오름차순으로 정렬
locate.sort()
# 초기화
ans = 0
left = 0
right = locate[-1] - locate[0]
# 이분탐색 코드 - 배치 가능한 공유기의 수가 필요한 공유기의 수보다 많은 경우는 공유기 사이의 길이를 늘리고
#                 그 반대인 경우는 공유기 사이의 길이를 줄인다
while left <= right:
    mid = (left+right)//2

    num = count(mid, locate)

    if num >= c:
        ans = max(ans, mid)
        left = mid + 1
    else:
        right = mid - 1

print(ans)
