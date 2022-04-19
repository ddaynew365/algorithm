N,L = map(int, input().split())
grid = []
for _ in range(N):
  grid.append(list(map(int, input().split())))

def construct(road, stairs, idx, direct):
  if direct:
    if idx + L > N:
      return (None, True)
    part = stairs[idx:idx+L]
  else:
    if idx - L + 1 < 0:
      return (None, True)
    part = stairs[idx-L+1:idx+1]
  
  num = road[idx]
  for i in range(len(part)):
    if part[i] == 1:
      return (None, True)
    if direct:
      if road[idx+i] != num:
        return (None, True)
      stairs[idx+i] = 1
    else:
      if road[idx-i] != num:
        return (None, True)
      stairs[idx-i] = 1
  return (stairs, False)

def is_road(road): 

  stairs = [0] * N
  fail = False
  for i in range(N-1):
    if road[i] == road[i+1]:
      continue
    elif road[i] - road[i+1] == 1:
      stairs, fail = construct(road, stairs, i+1, True)
    elif road[i] - road[i+1] == -1:
      stairs, fail =construct(road,stairs, i, False)
    else:
      return False

    if fail:
      return False
    
  for i in range(N-1):
    if road[i] == road[i+1] or road[i] == road[i+1]+stairs[i+1] or road[i]+stairs[i] == road[i+1]:
      continue
    else:
      return False
      
  return True

count = 0
for y in range(N):
  if is_road(grid[y]):
    count += 1

for x in range(N):
  temp = []
  for y in range(N):
    temp.append(grid[y][x])
  if is_road(temp):

    count += 1
print(count)