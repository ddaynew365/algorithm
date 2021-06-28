import sys
sys.setrecursionlimit(10**6)
N = int(input())
permutation = list(map(int,sys.stdin.readline().strip().split()))
result = []
prev_element = []

def dfs(element, destination):
    if len(element) == 0:
        result.append(prev_element[:])

    for e in element:
        if e != destination[len(prev_element)] and not result:
            continue
        if len(result) == 2:
            break
        print(e)
        next_element = element[:]
        next_element.remove(e)

        prev_element.append(e)
        dfs(next_element,destination)
        prev_element.pop()

dfs(list(range(1,N+1)), permutation)

if len(result) == 2:
    for i in result[1]:
        print(i ,end=' ')
else:
    print(-1)

