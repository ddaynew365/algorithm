N = int(input())
A = list(map(int, input().split()))
answer = [0] * N
stack = list()
for i in range(N):
  while stack and stack[-1][0] < A[i]:
    _, idx = stack.pop()
    answer[idx] = A[i]
  stack.append([A[i],i])

while stack:
  _, idx = stack.pop()
  answer[idx] = -1
  
for i in answer:
  print(i, end=" ")