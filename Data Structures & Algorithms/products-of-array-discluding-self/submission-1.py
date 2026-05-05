class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] = suffix * res[i] # As res[i] contains prefix
                                     # and final result is suffix * prefix
            suffix = suffix * nums[i]

        return res