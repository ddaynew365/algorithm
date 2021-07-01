from collections import defaultdict


def dfs(start, graph, length, answer):
    an = answer[:]
    an.append(start)

    if len(an) == length + 1:
        return an

    for idx, desti in enumerate(graph[start]):
        graph[start].pop(idx)

        ret = dfs(desti, graph, length, an)
        if ret:
            return ret
        graph[start].insert(idx, desti)


def solution(tickets):
    answer = []
    length = len(tickets)
    graph = defaultdict(list)

    for start, arrive in tickets:
        graph[start].append(arrive)

    for key, value in graph.items():
        graph[key] = sorted(value)

    answer = dfs("ICN", graph, length, answer)

    return answer