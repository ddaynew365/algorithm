# 크루스칼 알고리즘

# 이어진 노드 중 루트 노드를 반환(서로소 집합 자료구조)
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

# 두 개의 그래프를 합치는 함수(서로소 집합 자료구조)
def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# main 함수
def solution(n, costs):
    # 데이터 전처리
    answer = 0
    costs.sort(key = lambda x: x[2])
    select = []
    parent = [i for i in range(n)]
    # 크루스칼 알고리즘
    for i in costs:
        a, b = [i[0],i[1]]
        if find(parent, a) != find(parent,b):
            union(parent, a, b)
            answer += i[2]

    return answer
