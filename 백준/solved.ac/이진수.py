t = int(input())
for _ in range(t):
  n = int(input())
  bi = bin(n)[2:][::-1]
  for i in range(len(bi)):
    if bi[i] == "1":
      print(i, end =" ")
  print()