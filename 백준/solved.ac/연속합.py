n = int(input())
nums = list(map(int, input().split()))
idx = 0 
answer = cur = nums[0]
for i in range(1,len(nums)):
  if cur <= 0:
    cur = nums[i]
  else:
    cur += nums[i]
  answer = max(cur, answer)
print(answer)