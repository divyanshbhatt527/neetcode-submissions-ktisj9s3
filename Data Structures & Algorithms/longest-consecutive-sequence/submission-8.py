class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)<1:
            return 0
        
        sorted_list = sorted(set(nums))

        count = 1
        max_count = 1

        for i in range(1,len(sorted_list)):
            if (sorted_list[i]-1) == sorted_list[i-1]:
                count += 1
            else:
                count = 1
            
            max_count = max(max_count,count)

        return max_count
                
            

        
        

