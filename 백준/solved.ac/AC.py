from collections import deque
import re
t = int(input())
for _ in range(t):
  cmd = list(input())
  n = int(input())
  temp = input()
  p = re.compile("[0-9]+")
  arr =deque(p.findall(temp))
  fail, reverse = False, False
  for c in cmd:
    if c == 'R':
      reverse = not reverse
    else:
      if arr:
        if reverse:
          arr.pop()
        else:
          arr.popleft()
      else:
        print("error")
        fail = True
        break
  if not fail:
    if reverse:
      print('[' +','.join(list(arr)[::-1])+']')
    else:
      print('['+','.join(list(arr))+']')