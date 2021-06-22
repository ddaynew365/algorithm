from collections import defaultdict
import sys
num : int = int(input())
remains = defaultdict(int)

for _ in range(num):
    name, cmd = sys.stdin.readline().strip().split()
    if cmd == 'enter':
        remains[name] += 1
    else:
        remains[name] -= 1

answer = []
for key,value in remains.items():
    if value == 1:
        answer.append(key)

answer.sort(reverse=True)
for i in answer:
    print(i)

