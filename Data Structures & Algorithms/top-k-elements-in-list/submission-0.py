class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_count = {}
        for num in nums:
            if num not in freq_count:
                freq_count[num] = 1
            else:
                freq_count[num] += 1

        pairs = [(freq,ele) for ele,freq in freq_count.items()]
        pairs.sort(reverse=True)
        ans = [x[1] for x in pairs]

        ans = ans[:k]
        return ans        
        