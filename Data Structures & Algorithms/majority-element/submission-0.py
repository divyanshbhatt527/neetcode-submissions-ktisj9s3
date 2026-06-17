class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ele_freq = {}
        for num in nums:
            if num in ele_freq:
                ele_freq[num] += 1
            else:
                ele_freq[num] = 1

        maj_len = len(nums)//2
        max_freq = 0
        max_freq_ele = 0
        for k,v in ele_freq.items():
            if (v > maj_len) and (v >= max_freq):
                max_freq = v
                max_freq_ele = k

        return max_freq_ele
                