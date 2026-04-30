class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_count = {}
        for num in nums:
            if num not in freq_count:
                freq_count[num] = 1
            else:
                freq_count[num] += 1

        freq_arr = [[] for _ in range(len(nums)+1)]

        for ele,count in freq_count.items():
            freq_arr[count].append(ele)

        ans = []
        for i in range(len(freq_arr)-1,0,-1):
            for num in freq_arr[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans