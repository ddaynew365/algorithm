"""
초기풀이는 union_find 알고리즘을 사용하여 문제를 풀었다. 하지만 각 노드의 부모노드를
단순히 한단계 위의 노드로 선정을 하였기 때문에 시간 복잡도에 문제가 생겼다. 이를 해결하기 위해
메모리를 좀 더 사용하는 방향을 잡았다. 각 노드의 부모 노드를 트리의 루트 노드로 잡고 그대로 진행하였다.
결과적으로 시간복잡도가 10배 이상 효율적으로 개선되었다.
"""
# import sys
#
# n, m = map(int, input().split())
# tree = [-1] * (n+1)
# def find_parent(node):
#     temp = node
#     parent = tree[node]
#     flag = True
#     while parent != -1:
#         node = parent
#         parent = tree[node]
#         flag = False
#     if flag == False:
#         tree[temp] = node
#     return node
#
# for _ in range(m):
#     cmd, a, b = list(map(int,sys.stdin.readline().strip().split()))
#     pa, pb = find_parent(a), find_parent(b)
#     if cmd == 0:
#         if pa == pb:
#             continue
#         tree[pb] = pa
#     else:
#         if pa == pb:
#             print('YES')
#         else:
#             print('NO')

'''
재귀를 사용하여 모든 node의 부모를 루트 노드로 정하였다.
가장 빠른 속도를 보여주었다.
'''
import sys

n, m = map(int, input().split())
tree = [-1] * (n+1)
def find_parent(node):
    if tree[node] == -1:
        return node
    tree[node] = find_parent(tree[node])
    return tree[node]


for _ in range(m):
    cmd, a, b = list(map(int,sys.stdin.readline().strip().split()))
    pa, pb = find_parent(a), find_parent(b)
    if cmd == 0:
        if pa == pb:
            continue
        tree[pb] = pa
    else:
        if pa == pb:
            print('YES')
        else:
            print('NO')