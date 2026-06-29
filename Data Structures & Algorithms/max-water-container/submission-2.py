class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_res = 0
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                area = min(heights[i],heights[j]) * (j-i)
                max_res = max(area,max_res)

        return max_res