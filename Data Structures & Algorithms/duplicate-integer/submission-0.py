class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = dict()
        for i in range(0,len(nums)):
            if nums[i] in d:
                return True
            else:
                d[nums[i]]=i
        return False

