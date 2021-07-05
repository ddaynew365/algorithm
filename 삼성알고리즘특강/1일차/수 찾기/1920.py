from collections import defaultdict
N = int(input())
N_list = list(map(int, input().strip().split()))
M = int(input())
M_list = list(map(int, input().strip().split()))

N_dict = defaultdict(int)
for n in N_list:
    N_dict[n] += 1

for m in M_list:
    if N_dict[m] > 0:
        print(1)
    else:
        print(0)