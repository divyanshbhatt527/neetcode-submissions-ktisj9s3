class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first_index = -1
        last_index = -1
        if len(nums) == 1 and nums[0] == target:
            return [0,0]
        low = 0
        high = len(nums) - 1
        # Getting first index
        while low<=high:
            mid = (low+high)//2
            if nums[mid] == target:
                high = mid - 1
                first_index = mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        
        low = 0
        high = len(nums) - 1
        # Getting last index
        while low<=high:
            mid = (low+high)//2 
            if nums[mid] == target:
                low = mid + 1
                last_index = mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

            
        return [first_index, last_index]