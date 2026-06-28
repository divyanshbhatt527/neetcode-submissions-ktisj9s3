class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        max_count = 0
        for num in nums:
            count = 1
            curr = num
            if (num-1) in hashset:
                continue
            while (curr+1) in hashset:
                count += 1
                curr += 1 
            max_count = max(count,max_count)

        return max_count