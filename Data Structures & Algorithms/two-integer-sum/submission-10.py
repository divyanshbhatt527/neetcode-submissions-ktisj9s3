class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        # target = nums[i] + nums[j]
        # nums[j] = target - nums[i]
        # storing result as key and index as value in the hashmap
        for i in range(len(nums)):
            res = target - nums[i]
            if res in hash_map:
                return [hash_map[res],i]
            else:
                hash_map[nums[i]] = i