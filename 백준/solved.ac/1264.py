import re
while True:
  str = input()
  if str == "#":
    break
  p = re.compile("[aeiou]")
  arr = p.findall(str.lower())
  print(len(arr))