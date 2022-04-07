import re
a = input()
b = input()

p = re.compile(b)
arr = p.findall(a)
print(len(arr))
