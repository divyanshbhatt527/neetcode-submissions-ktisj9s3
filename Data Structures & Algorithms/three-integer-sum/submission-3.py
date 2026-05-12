class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = set()
        for i, a in enumerate(nums):
            j = i+1
            k = len(nums)-1
            while j<k:
                if a+nums[j]+nums[k] == 0:
                    ans.add(tuple([a,nums[j],nums[k]]))
                    j += 1
                elif a+nums[j]+nums[k] > 0:
                    k -= 1
                else:
                    j += 1
        return list(ans)
