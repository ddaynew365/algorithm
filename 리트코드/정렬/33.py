from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 피벗 구하기
        pivot = 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i + 1]:
                pivot = i + 1
                break
        # target 위치 구하기                
        s_nums = sorted(nums)
        
        origin_locate = -1
        lo = 0
        hi = len(s_nums) - 1
        while lo <= hi:
            m = (lo + hi) // 2
            if s_nums[m] == target:
                origin_locate = m 
                break
            elif s_nums[m] < target:
                lo = m + 1
            elif s_nums[m] > target:
                hi = m - 1
        if origin_locate == -1:
            return -1
        # 답 구하기
        answer = origin_locate + pivot
        
        if answer > len(nums) - 1:
            answer -= len(nums)
                            
        return answer