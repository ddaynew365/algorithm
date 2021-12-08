'''
단순 구현 풀이
'''
def find_next_num(num : int, P : int) -> int:
    num_list = list(str(num))
    sum = 0
    for i in num_list:
        sum += int(i)**P
    return sum


A, P = map(int, input().split())

arr = list()

arr.append(A)

while True:
    next_num = find_next_num(arr[-1], P)
    if next_num in arr:
        idx = arr.index(next_num)
        arr = arr[:idx]
        break
    arr.append(next_num)

print(len(arr))