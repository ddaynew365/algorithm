total = 0
move = []
answer = total
for _ in range(10):
  down, up=map(int, input().split())
  total = total - down + up
  answer = max(total, answer)

if answer > 10000:
  print(10000)
else:
  print(answer)