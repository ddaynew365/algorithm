import re, sys
input = sys.stdin.readline
t = int(input())
p = re.compile('(100+1+|01)+')
for _ in range(t):
  ele=input().rstrip()
  if p.fullmatch(ele):
    print("YES")
  else:
    print("NO")