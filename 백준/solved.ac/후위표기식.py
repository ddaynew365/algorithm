word = list(input())
pri = {"*":1, "/":1, "+":2, "-":2}
open = 0
stack = []
answer = ""
for char in word:
  if char.isalpha():
    answer += char
  else:
    if char == "(":
      stack.append(char)
    elif char == ")":
      while stack and stack[-1] != "(":
        answer += stack.pop()
      stack.pop()
    else:
      while stack and stack[-1] in pri and pri[char] >= pri[stack[-1]]:
        answer += stack.pop()
      stack.append(char)

while stack:
  answer += stack.pop()
print(answer)
        
    
    
    