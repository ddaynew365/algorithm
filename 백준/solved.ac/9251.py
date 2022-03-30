str1 = input()
str2 = input()
lcs = [[0 for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]

for i in range(len(str1) + 1):
  for j in range(len(str2) + 1):
    if i ==0 or j ==0:
      continue
    elif str1[i-1] == str2[j-1]:
      lcs[i][j] = lcs[i-1][j-1] + 1
    elif str1[i-1] != str2[j-1]:
      lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])
answer  = 0  
for i in range(len(str1) + 1):
  for j in range(len(str2)+ 1):
    answer = max(answer, lcs[i][j])
print(answer)

i, j = len(str1), len(str2)
result = []
while lcs[i][j] != 0:
  if lcs[i][j] == lcs[i-1][j]:
    i = i-1
  elif lcs[i][j] == lcs[i][j-1]:
    j = j-1
  else:
    i,j = i-1, j-1
    result.append(str1[i])

print(result[::-1])