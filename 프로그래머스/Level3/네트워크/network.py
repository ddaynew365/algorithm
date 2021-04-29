"""
이번 문제는 깊이 탐색 알고리즘의 전형적인 문제였다. 모든 노드에 dfs 함수를 한번씩 넣어서 해당 노드가 방문한적이 없고 연결된 다른 노드가 있으면 하나의 네트워크를 발견한 것이라고 생각하여
아래와 같은 코드를 만들었다
"""
# dfs 알고리즘
def dfs(computers, visited, v):
    #방문했던 노드면 False 
    if visited[v] == 1:
        return (False, visited)
    #처음 방문한 노드인 경우
    visited[v] = 1
    # 연결된 다른 노드 찾기
    for i in range(len(visited)):
        if i == v:
            continue
            print(v,i, visited)         
        if computers[v][i] ==1:
            dfs(computers, visited, i)
    # 하나의 네트워크에 끝에 다다르면 True를 반환
    return (True, visited)
    
            
    
def solution(n, computers):
    answer = 0
    visited = [0] * n
    # 모든 노드에 대해서 dfs 탐색을 하여 새로운 네트워클 찾으면 값을 1 증가
    for num in range(n):
        bools, visited = dfs(computers, visited, num)
        if bools == True:
            
            answer += 1
    
    return answer
