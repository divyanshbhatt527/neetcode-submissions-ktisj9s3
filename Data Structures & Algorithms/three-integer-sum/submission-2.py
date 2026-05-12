class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = set()
        for i in range(len(nums)):
            j = i+1
            k = len(nums)-1
            target = -nums[i]
            while j<k:
                sum_ele = nums[j]+nums[k]
                if sum_ele == target:
                    ans.add(tuple([nums[i],nums[j],nums[k]]))
                    j += 1
                    
                elif sum_ele < target:
                    j += 1
                else:
                    k -= 1
        return list(ans)
