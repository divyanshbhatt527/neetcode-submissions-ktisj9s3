class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # target = nums[i] + nums[j]
        # nums[j] = target - nums[i]

        hashmap = {}
        for i in range(len(nums)):
            ele = target - nums[i]
            if ele in hashmap:
                return [hashmap[ele],i]

            else:
                hashmap[nums[i]] = i


        