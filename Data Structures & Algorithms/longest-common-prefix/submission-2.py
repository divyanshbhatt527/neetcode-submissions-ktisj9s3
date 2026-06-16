class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        min_word = min(strs, key=len)
        flag = True
        for i in range(len(min_word)):
            for j in range(len(strs)):
                if min_word[i] != strs[j][i]:
                    flag = False
                
            if flag:
                res += min_word[i]
            else:
                break
        return res

            

        return res