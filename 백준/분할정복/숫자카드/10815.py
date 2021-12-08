# from collections import defaultdict
# import sys
# answer:list[int] = list()
# n_num: int = int(sys.stdin.readline())
# n_array: list[int] = list(map(int, sys.stdin.readline().strip().split()))
# m_num: int = int(sys.stdin.readline())
# m_array: list[int] = list(map(int, sys.stdin.readline().strip().split()))

# hash: dict[int, int] = defaultdict(int)
# for n in n_array:
#   hash[n] += 1

# for m in m_array:
#   hash[m] -= 1

# for m in m_array:
#   if hash[m] == 0:
#     answer.append(1)
#   else:
#     answer.append(0)
    
# for i in answer:
#   print(i, end = ' ')



import sys
n_num: int = int(sys.stdin.readline())
n_array: list[int] = list(map(int, sys.stdin.readline().strip().split()))
print(n_array)
n_array:set[int] = set(n_array)
print(n_array)
m_num: int = int(sys.stdin.readline())
m_array: list[int] = list(map(int, sys.stdin.readline().strip().split()))

for m in m_array:
    if m in n_array:
        print("1", end = " ")
    else:
        print("0", end= " ")