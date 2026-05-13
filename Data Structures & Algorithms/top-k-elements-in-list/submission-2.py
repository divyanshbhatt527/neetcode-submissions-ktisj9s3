class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1

        res = [(f,v) for v,f in freq.items()]
        res.sort(reverse=True)
        ans = [ele[1] for ele in res]
        return ans[:k]


        

        
