class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = height[0]
        water = 0
        for i in range(1,len(height)-1):
            right_max = 0
            
            for j in range(i+1,len(height)):
                right_max = max(right_max,height[j])

            curr = min(left_max,right_max) - height[i]
            water += 0 if curr < 0 else curr
            
            left_max = max(left_max,height[i])

        return water
            

