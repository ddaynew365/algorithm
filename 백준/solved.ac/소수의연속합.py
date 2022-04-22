n = int(input())
sqrt = int(n ** (1/2))
era = [True] *(n+1)
era[0] = era[1] = False
for i in range(2, sqrt+1):
  if era[i]:
    for j in range(2*i, n+1,i):
      era[j] = False
sosu = [i for i in range(n+1) if era[i]]

lo = hi = 0
total = 0
length = len(sosu)
success = False
count = 0
while hi < length:
  total += sosu[hi]
  while total > n:
    total -= sosu[lo]
    lo += 1
  if total == n:
    count += 1
  hi += 1

print(count)