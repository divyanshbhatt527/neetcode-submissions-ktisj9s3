class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # area = length(min(heights[i],heights[j]) * breadth(j-i)
        max_area = 0
        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                l = min(heights[i],heights[j])
                b = j-i
                area = l*b
                max_area = max(area,max_area)

        return max_area