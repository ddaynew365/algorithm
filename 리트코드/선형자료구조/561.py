# 561. Array Partition 1
# 처음 문제를 보자마자 인덱스가 짝수인 수들의 합을 구하면 된다고 생각하였다
# 하지만 리스트의 원소 수가 홀수인 경우 당연히 뒤에서부터 세면 인덱스가 홀수인 수들의 합이라고 생각하였다

class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        nums.sort()
        length = len(nums)
        if length % 2 == 0:
            return sum([nums[i] for i in range(length) if i%2 ==0])
        else:
            return sum([nums[i] for i in range(length) if i%2 ==1]) 

# 하지만 해당 문제는 무조건 짝수의 개수만 가지는 전제를 가지고 있었고 아래와 같은 방법으로 짝수 인덱스의 합을
# 파이썬틱하게 구할 수 있었다.          
class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:          
      return sum(sorted(nums)[::2])