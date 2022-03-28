import re
while True:
  str = input()
  if str == "EOI":
    break
  if re.search("nemo", str.lower()):
    print("FOUND")
  else:
    print("Missing")