class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1

        res = [[] for _ in range(len(nums)+1)]
        for ele,count in freq.items():
            res[count].append(ele)
        ans = []
        for i in range(len(res)-1,0,-1):
            for ele in res[i]:
                if k>0:
                    ans.append(ele)
                    k -= 1
        return ans


        

        
