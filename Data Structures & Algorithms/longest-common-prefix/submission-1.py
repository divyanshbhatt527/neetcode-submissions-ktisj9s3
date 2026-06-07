class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        min_str = min(strs,key=len)
        min_len = len(min_str)

        for i in range(len(min(strs))):
            curr_chr = ''
            flag = True
            for j in range(len(strs)):
                if curr_chr == '':
                    curr_chr = strs[j][i]
                else:
                    if strs[j][i] == curr_chr:
                        continue
                    else:
                        flag = False
                        break
            if flag:
                res += curr_chr
            else:
                break

        return res
                
        
        



