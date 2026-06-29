class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # move pointer with smaller height to get max area covered
        max_res = 0
        i = 0
        j = len(heights) - 1
        
        while i < j:
            area = min(heights[i],heights[j])*(j-i)
            max_res = max(area,max_res)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1

        return max_res