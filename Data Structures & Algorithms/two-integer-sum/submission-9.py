class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # can't sort directly because the ord of indices will change
        # nums[i]+nums[j] = target
        # nums[j] = target-nums[i]

        hashmap = {}
        for i in range(len(nums)):
            if (target - nums[i]) in hashmap:
                return [hashmap[target-nums[i]],i]
            else:
                hashmap[nums[i]] = i

        