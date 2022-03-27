m, n = map(int, input().split(" "))

era = [True] * (n+1)
era[0] = False
era[1] = False
for i in range(2, int((n**(1/2)) + 1)):
  val = 2* i
  while val < n+1:
    era[val] = False
    val += i

for i in range(m, n+1):
  if era[i] == True:
    print(i)