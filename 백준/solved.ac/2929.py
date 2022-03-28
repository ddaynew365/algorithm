str = input()
answer = 0
j = 0
for i in range(len(str)):
  if str[i].isupper() and j % 4 != 0:
    answer += (4 -(j %4))
    j += (4- (j%4))
  j += 1
print(answer)