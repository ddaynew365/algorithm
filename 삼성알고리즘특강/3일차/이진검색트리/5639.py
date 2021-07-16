import sys
def recur(s, e):
    if s == e:
        print(graph[s])
    else:
        where = s + 1
        while where <= e:
            if graph[where] > graph[s]:
                break
            where += 1
        # left
        recur(s + 1, where-1)
        # right
        recur(where,e)
        print(graph[s])
graph = []
i = 0
while(i<10000):
    try:
        graph.append(int(sys.stdin.readline()))
        i == 1
    except:
        break

recur(0, len(graph)-1)

