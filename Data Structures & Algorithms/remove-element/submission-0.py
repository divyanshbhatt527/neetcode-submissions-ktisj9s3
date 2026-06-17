class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                k += 1 
                nums[i],nums[j] = nums[j],nums[i]
                i += 1
        return k