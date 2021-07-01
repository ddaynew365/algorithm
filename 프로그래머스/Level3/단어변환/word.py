"""
해당 문제를 푸는데 있어 dfs와 bfs 중 어떠한 알고리즘을 써야하는지에 대해 많은 고민을 하였다. 처음에는 dfs를 사용하여 문제를 해결하려고 했으나 가는 과정의 최솟값을 구하는게
매우 힘들다는 것을 알았다. 하지만 프로그래머스 사이트의 테스트케이스 부족에 의해 해당 코드가 통과를 해버렸다. 아래의 코드는 해당 단어로의 모든 경로가 아닌 단 하나의 경로의
길이만을 구하는 기능을 가지고 있지만 테스트케이스의 부족으로 통과한 코드다.
또한 dfs는 구현 방식이 재귀 방식과 stack(파이썬에서는 리스트) 방식이 있는 재귀 방식 구현에 대해서는 아직 부족한 부분이 많다는 것을 느꼈다. 특히 for문으로 동시에 여러개로 갈라지는
재귀함수의 경우 어떠한 값이 반환되는지에 대해 많은 공부가 필요할 것 같다.
"""
# def solution(begin, target, words):
#     #stack으로 구현
#     answer = 0
#     stack = [begin]
#     visited = []
#
#     if target not in words:
#         return 0
#
#     while stack:
#         curr = stack.pop()
#         if curr == target:
#             return answer
#
#         for w in words:
#             if len([i for i in range(0,len(w)) if w[i]!=curr[i]]) == 1:
#                 if w in visited:
#                     continue
#
#                 visited.append(w)
#                 stack.append(w)
#         print(curr, stack, answer)
#         answer += 1
#     return answer
  
'''
이에 탐색의 최소길이를 구하는 문제는 대체로 bfs가 유용하다는 것을 꺠닫고 stack을 queue로 바꿔서 문제를 해결한 코드다. 하나의 노드에 접근할 때마다 그 다음 갈 수 있는 노드들을
queue에 넣고 각각의 길이를 따져서 구하였다.
'''
# from collections import deque
#
# def solution(begin, target, words):
#     answer = {}
#     queue = deque()
#     queue.append(begin)
#     visited = []
#
#     if target not in words:
#         return 0
#
#     answer[begin] = 0
#
#     while queue:
#         curr = queue.popleft()
#         if curr == target:
#             return answer.get(target, 0)
#
#         for w in words:
#             if len([i for i in range(0,len(w)) if w[i]!=curr[i]]) == 1:
#                 if w in visited:
#                     continue
#
#                 visited.append(w)
#                 queue.append(w)
#                 answer[w] = answer[curr] +1


'''
각각 기능별 함수로 쪼개어 좀 더 구조적인 코드가 되게 만들었다 
'''
from collections import deque


def diff_oneletter(word, cur):
    count = 0

    for w_char, c_char in zip(word, cur):
        if w_char != c_char:
            count += 1

        if count >= 2:
            break

    if count == 1:
        return True
    else:
        return False


def bfs(begin, target, words):
    queue = deque([begin])
    visited = {}
    visited[begin] = 0

    while queue:
        cur = queue.popleft()
        if cur == target:
            break

        for word in words:
            if word not in visited and diff_oneletter(word, cur) == True:
                queue.append(word)
                visited[word] = visited[cur] + 1

    if target not in visited:
        return 0
    else:
        return visited[target]


def solution(begin, target, words):
    answer = 0
    answer = bfs(begin, target, words)
    return answer
