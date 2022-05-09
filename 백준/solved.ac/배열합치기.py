from heapq import heappop, heappush
A, B = map(int,input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
answer = []
# i, j = 0, 0
# while i < A and j < B:
#   if a[i] <= b[j]:
#     answer.append(a[i])
#     i += 1
#   else:
#     answer.append(b[j])
#     j += 1
# if i == A:
#   answer += b[j:] 
# else:
#   answer += a[i:]

# for num in answer:
#   print(num, end=' ')

for num in a:
  heappush(answer,num)
for num in b:
  heappush(answer,num)


while answer:
  print(heappop(answer), end=' ')