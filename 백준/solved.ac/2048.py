import sys
sys.setrecursionlimit(10**6)
n = int(input())
maps = []
for _ in range(n):
  maps.append(list(map(int, input().split())))
max_num = 0
move = [(1,0),(-1,0),(0,1),(0,-1)]
def make_queue(stack):
  queue = []
  while stack:
    f = stack.pop()
    if stack:
      s = stack.pop()
      if f == s:
        queue.append(f+s)
      else:
        queue.append(f)
        stack.append(s)
    else:
      queue.append(f)
  return queue

def dfs(maps, count):
  if count == 5:
    num = max(map(max,maps))
    global max_num
    max_num = max(max_num, num)
    return
  for dy, dx in move:
    stack = []
    queue = []
    if dx == 0:
      if dy == 1:
        graph= [y[:] for y in maps]
        for x in range(n):
          for y in range(n):
            if graph[y][x] != 0:
              stack.append(graph[y][x])
              graph[y][x] = 0
          queue = make_queue(stack)
          for i in range(len(queue)):
            graph[n-1-i][x] = queue[i]
        dfs(graph, count + 1)
      else:
        graph= [y[:] for y in maps]
        for x in range(n):
          for y in range(n-1,-1,-1):
            if graph[y][x] != 0:
              stack.append(graph[y][x])
              graph[y][x] = 0
          queue = make_queue(stack)
          for i in range(len(queue)):
            graph[i][x] = queue[i]
        dfs(graph, count + 1)
    else:
      if dx == 1:
        graph= [y[:] for y in maps]
        for y in range(n):
          for x in range(n):
            if graph[y][x] != 0:
              stack.append(graph[y][x])
              graph[y][x] = 0
          queue = make_queue(stack)
          for i in range(len(queue)):
            graph[y][n-i-1] = queue[i]
        dfs(graph, count + 1)            
      else:
        graph= [y[:] for y in maps]
        for y in range(n):
          for x in range(n-1,-1,-1):
            if graph[y][x] != 0:
              stack.append(graph[y][x])
              graph[y][x] = 0
          queue = make_queue(stack)
          for i in range(len(queue)):
            graph[y][i] = queue[i]
        dfs(graph, count + 1)            

dfs(maps, 0)
print(max_num)