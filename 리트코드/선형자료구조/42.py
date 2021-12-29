class Solution:
    def trap(self, height: list[int]) -> int:
        if not height:
            return 0
        answer = 0
        left, right = 0 , len(height) - 1
        leftmax = height[left]
        rightmax = height[right]
        
        while left < right:
            leftmax = max(leftmax, height[left])
            rightmax = max(rightmax, height[right])
            if leftmax <= rightmax:
                answer += leftmax - height[left]
                left += 1
            else:
                answer += rightmax - height[right]
                right -= 1
        return answer
      
# 투포인터를 사용한 방법 -> 결국 하나의 인덱스에서 왼쪽 오른쪽 모두를 비교하였을 때, 둘 다 자신보다 높으면 그
# 둘 중 더 낮은 쪽만큼 물이 채워진다는 방식을 이용하였다.