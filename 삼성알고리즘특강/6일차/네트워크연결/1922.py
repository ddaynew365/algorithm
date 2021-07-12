"""
해당 문제는 최소 신장트리를 구하는 문제다
여기서 크루스칼 알고리즘과 프림 알고리즘이 존재하는데 크루스칼은 union-find 알고리즘을 사용하여
순환을 탐색하는 것에 중점을 두고
프림 알고리즘은 다익스트라 알고리즘과 유사하게 최소 힙을 사용하는 것에 중점을 두는 알고리즘이다.
"""

'''
첫번째 문제는 크루스칼 알고리즘을 사용하였다.
'''
import sys
def find(node):
    if parent[node] == node:
        return node
    parent[node] = find(parent[node])
    return parent[node]

def union(a,b):
    pa = find(a)
    pb = find(b)
    parent[pb] = pa

# 데이터 입력
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = []
parent = [i for i in range(n+1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    graph.append([c,a,b])
# 크루스칼 알고리즘을 위한 정렬
graph.sort(key = lambda x: x[0])
# 오름차순으로 하나씩 탐색하면서 순환이 생기는 간선은 배제
total = 0
count = 0
for value, a, b in graph:
    if count == (n-1):
        break
    if find(a) == find(b):
        continue
    else:
        union(a,b)
        total += value
        count += 1

print(total)

'''
프림 알고리즘
'''
import heapq

