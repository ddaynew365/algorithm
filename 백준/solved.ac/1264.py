import re
while True:
  str = input()
  if str == "#":
    break
  p = re.compile("[aeiou]", re.I)
  arr = p.findall(str)
  print(len(arr))