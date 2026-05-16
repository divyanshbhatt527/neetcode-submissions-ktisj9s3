class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = [0]*len(height)
        right_max = [0]*len(height)

        prefix = height[0]
        for i in range(1,len(height)):
            left_max[i] = prefix
            prefix = max(prefix,height[i])

        suffix = height[-1]
        for j in range(len(height)-1,-1,-1):
            right_max[j] = suffix
            suffix = max(suffix,height[j])

        water = 0
        for i in range(len(height)):
            curr = min(left_max[i],right_max[i]) - height[i]
            water += 0 if curr < 0 else curr

        return water
            

