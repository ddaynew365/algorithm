def farctional_knapsack(cargo):
  capacity = 15
  pack = []
  answer = 0
  for c in cargo:
    pack.append([c[0]/c[1],c[0],c[1]])
  
  pack.sort()
  while capacity != 0:
    cur = pack.pop()
    if capacity > cur[2]:
      capacity -= cur[2]
      answer += cur[1]
    else:
      answer += cur[0] * capacity
      capacity = 0
      
  return answer




cargo = [
  (4, 12),
  (2, 1),
  (10, 4),
  (1, 1),
  (2, 2)
]

r = farctional_knapsack(cargo)
print(r)
