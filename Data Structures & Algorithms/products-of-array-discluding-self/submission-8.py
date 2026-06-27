class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prefix = 1
        for num in nums:
            res.append(prefix)
            prefix *= num

        print(res)
        suffix = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= suffix
            suffix *= nums[i]
        print(res)

        return res 