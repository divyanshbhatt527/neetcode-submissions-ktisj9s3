class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = {}
        for i in range(len(nums)):
            ele = target - nums[i]
            if ele in hashmap:
                return [hashmap[ele],i]
            else:
                hashmap[nums[i]] = i