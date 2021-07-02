"""
처음 풀이때는 단순히 dfs로 순열을 구현하여 문제를 해결해보려 하였다. 하지만 입력값이 매우 커서 시간 초과가 발생하였다. 이를 줄이기 아래 코드와
같이 백트레킹을 사용해보았다. 하지만 이 역시 시간초과가 발생하였다. 그 후 구글링을 통하여 C++에 있는 next_permutation 함수를 구현하는
알고리즘을 찾아냈다.

다음 순열 구하는 알고리즘
예시) 1 4 3 2
1. 뒤에서부터 순열을 비교하며, 뒷 값이 앞 값보다 큰 경우까지 반복한다. (3,2), (4,3)은 해당하지 않고,  (1,4)가 해당된다.
- 이 떄, 1의 인덱스를 x라고 칭한다.
- 4의 인덱스는 y라고 한다.
2. 다시 뒤에서부터 값을 비교하며 인덱스 x보다 큰 값이 있으면 그 값과 swap한다.
- 1과 2를 비교했고, 2가 크기 때문에 이 둘을 swap한다.
3. y에 해당되는 인덱스부터 sort를 한 뒤에 이어 붙인다.
- 4 3 1을 sorr하여 1 3 4가 된다
- 이어 붙이기 때문에 2 1 3 4가 된다.
[출처: https://codedrive.tistory.com/386, CodeDrive님의 티스토리]
"""
'''
첫번째 코드 - 백트레킹을 사용한 순열 구하는 알고리즘(시간 초과)
'''
# import sys
# sys.setrecursionlimit(10**6)
# N = int(input())
# permutation = list(map(int,sys.stdin.readline().strip().split()))
# result = []
# prev_element = []
# # dfs를 사용하여 모든 순열을 구하는 함수
# def dfs(element, destination):
#     if len(element) == 0:
#         result.append(prev_element[:])
#
#     for e in element:
#         if e != destination[len(prev_element)] and not result:
#             continue
#         if len(result) == 2:
#             break
#         print(e)
#         next_element = element[:]
#         next_element.remove(e)
#
#         prev_element.append(e)
#         dfs(next_element,destination)
#         prev_element.pop()
#
# dfs(list(range(1,N+1)), permutation)
#
# if len(result) == 2:
#     for i in result[1]:
#         print(i ,end=' ')
# else:
#     print(-1)

'''
두번째 코드 - next_permutation 구현 알고리즘
'''
N = int(input())
arr = list(map(int, input().split()))

# 1. 뒤에서부터 뒷값이 앞 값보다 큰 인덱스 찾기
find1, find2 = False, False
for i in range(N-1,0,-1):
    if arr[i-1] < arr[i]:
        f_idx = i -1
        find1 = True
        break

if find1 == True:
    for j in range(N-1,0,-1):
        if arr[j] > arr[f_idx]:
            arr[j],arr[f_idx] = arr[f_idx],arr[j]
            find2 = True
            break

if find2 == True:
    answer = arr[:f_idx + 1] + sorted(arr[f_idx + 1:])
    for an in answer:
        print(an, end=' ')
else:
    print(-1)

