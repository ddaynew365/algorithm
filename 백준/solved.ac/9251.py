import sys
input = sys.stdin.readline
str1 = input().strip()
str2 = input().strip()

n = len(str1)
m = len(str2)
lcs = [[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(n+1):
  for j in range(m+1):
    if i == 0 or j == 0:
      lcs[i][j] == 0
    elif str1[i-1] == str2[j-1]:
      lcs[i][j] = lcs[i-1][j-1] + 1
    else:
      lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])

answer = 0
for i in range(n+1):
  for j in range(m+1):
    answer = max(answer, lcs[i][j])
print(answer)
i = n
j = m    
result = []
while lcs[i][j] != 0:
  if lcs[i][j] == lcs[i-1][j]:
    i = i-1
  elif lcs[i][j] == lcs[i][j-1]:
    j = j-1
  else:
    result.append(str1[i-1])
    i, j = i-1,j-1
    
print(result[::-1])