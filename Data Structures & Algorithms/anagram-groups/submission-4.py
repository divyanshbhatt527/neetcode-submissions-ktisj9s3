class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_ans = {}
        for word in strs:
            count = [0]*26
            for w in word:
                index = ord(w) - ord('a')
                count[index] += 1
            if tuple(count) in final_ans:
                final_ans[tuple(count)].append(word)
            else:
                final_ans[tuple(count)] = [word]

        return list(final_ans.values())
        
        

        