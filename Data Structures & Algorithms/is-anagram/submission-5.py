class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_arr = [0]*26
        

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            ord_chr_s = ord(s[i]) - ord('a')
            ord_chr_t = ord(t[i]) - ord('a')
            
            freq_arr[ord_chr_s] += 1
            freq_arr[ord_chr_t] -= 1

        return all(x == 0 for x in freq_arr)