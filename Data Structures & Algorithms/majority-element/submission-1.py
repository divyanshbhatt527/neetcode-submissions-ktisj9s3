class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ele_freq = defaultdict(int)
        max_count = 0
        n = len(nums)//2
        for num in nums:
            ele_freq[num] += 1
            if ele_freq[num] > max_count:
                max_count = ele_freq[num]
                
            if max_count > n:
                return num
                