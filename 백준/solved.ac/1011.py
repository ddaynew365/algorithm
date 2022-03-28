T = int(input())
case = []
for _ in range(T):
  case.append(list(map(int, input().split(" "))))
  
  
for start, end in case:
  dist = end- start
  sqrt = int(dist**(1/2))
  if sqrt ** 2 == dist:
    print(sqrt*2-1)
  elif sqrt ** 2 < dist <= (sqrt **2) + sqrt:
    print(sqrt*2)
  else:
    print((sqrt+1) *2 -1)
  