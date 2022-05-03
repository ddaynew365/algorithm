N, r ,c = map(int,input().split())
answer = 0 
while N != 0:
  if r >= 2**(N-1):
    r -= 2**(N-1)
    answer += 2**(2*(N-1)+1)
  if c >= 2**(N-1):
    c -= 2**(N-1)
    answer += 2**(2*(N-1))
  N -= 1

print(answer)
