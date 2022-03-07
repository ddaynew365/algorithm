# 배낭 문제에서 물건을 쪼갤 수 있을 경우, 그리디로 푸는 게 가능하다. 하지만 쪼개지 못할 경우, 다이나믹 프로그래밍(dp)로 풀어야 한다.
# 비슷한 예로 우리나라의 동전문제가 있다. 우리나라처럼 배수의 동전만 있는 경우 그리디로 가능하지만 배수의 동전만 있는 것이 아닌 경우, DP로 풀어야 한다.
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
