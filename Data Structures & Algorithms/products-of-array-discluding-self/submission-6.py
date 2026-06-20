class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        prefix_arr = [0]*len(nums)
        for i in range(len(nums)):
            prefix_arr[i] = prefix
            prefix *= nums[i]
        print(prefix_arr)
        suffix = 1
        res = [0]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            res[i] = suffix * prefix_arr[i]
            suffix *= nums[i]


        return res