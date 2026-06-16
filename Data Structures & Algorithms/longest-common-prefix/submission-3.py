class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        min_word = min(strs, key=len)
        
        for i in range(len(min_word)):
            for j in range(len(strs)):
                if min_word[i] != strs[j][i]:
                    return res
            res += min_word[i]
            
        return res