class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i in range(0, len(nums)):
            d = target - nums[i]
            if d in hm:
                return [hm[d],i]
            else:
                hm[nums[i]] = i