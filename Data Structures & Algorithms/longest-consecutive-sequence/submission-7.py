class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)<1:
            return 0
        hashset = set()
        for i in nums:
            hashset.add(i)
        max_count = 1
        for num in nums:
            count = 1
            if num-1 not in hashset:
                ele = num+1
                while ele in hashset:
                    count += 1
                    ele += 1
                max_count = max(max_count, count)
            else:
                continue 
        return max_count
                
            

        
        

