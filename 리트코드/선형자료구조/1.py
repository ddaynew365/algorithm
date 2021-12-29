# 브루트 포스 방식 (이중 for문) 4100ms
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
# combination 사용            3232ms
from itertools import combinations
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        comb = combinations(nums, 2)
        for x,y in comb:
            if x + y == target:
                return [nums.index(x), nums.index(y,nums.index(x)+1)]
              
# 리스트를 사용하여 target - num 이 nums에 있는지를 파악하는 방법(결국 O(N2)긴하다) 632ms
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for idx, val in enumerate(nums):
            tar = target - val
            if tar in nums[idx+1:]:
                return [idx, nums.index(tar, idx+1)]
# 딕셔너리를 사용한 방법 56ms              
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_map = {}
        for idx, num in enumerate(nums):
            nums_map[num] = idx
        
        for idx, num in enumerate(nums):
            if target - num in nums_map and nums_map[target - num] != idx:
                return [idx, nums_map[target - num]]

                
                