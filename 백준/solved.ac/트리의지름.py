from collections import deque
v = int(input())
tree = [[] for _ in range(v+1)]
for _ in range(v):
  node, *arr, end = map(int,input().split())
  for i in range(len(arr)):
    if i % 2== 0:
      to = arr[i]
    else:
      cost = arr[i]
      tree[node].append((to, cost))

# def bfs(start):
#   visit = []
#   queue = deque()
#   queue.append((0, start))
  
#   answer = [0,start]
#   while queue:
#     cost, cur = queue.popleft()
#     visit.append(cur)
#     for next, ncost in tree[cur]:
#       if next not in visit:
#         total = cost + ncost
#         if answer[0] < total:
#           answer = [total, next]
#         queue.append((total, next))
#   return answer
visit = [1]
answer = 0
node = -1
def dfs(cur, cost):
  global answer, node
  if cost > answer:
    answer = cost
    node = cur
  for next, ncost in tree[cur]:
    if next not in visit:
      visit.append(next)
      dfs(next, ncost+cost)
      visit.pop()
  
  
dfs(1,0)
one, answer = answer, 0
a, node = node, -1
visit = [a]
dfs(a, 0)
print(max(one, answer))
    
  
