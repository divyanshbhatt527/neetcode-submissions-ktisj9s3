class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = 0
        index = -1
        res = [0]*len(nums)
        product = 1
        
        for i, n in enumerate(nums):
            if n == 0:
                zero_count += 1
                index = i
            else:
                product *= n

        if zero_count >= 2:
            return res
        
        elif zero_count == 1:
            res[index] = product
            return res
        else:
            for i in range(len(nums)):
                res[i] = product//nums[i]
            return res

            


        