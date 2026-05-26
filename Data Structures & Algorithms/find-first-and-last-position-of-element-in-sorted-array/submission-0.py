class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first_index = -1
        last_index = -1
        for index, ele in enumerate(nums):
            if (ele == target) and (first_index<0):
                first_index = index
            if (ele == target) and (first_index>=0):
                last_index = index
            
        return [first_index, last_index]