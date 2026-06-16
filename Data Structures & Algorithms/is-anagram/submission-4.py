class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_arr_1 = [0]*26
        freq_arr_2 = [0]*26

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            ord_chr_s = ord(s[i]) - ord('a')
            ord_chr_t = ord(t[i]) - ord('a')
            
            freq_arr_1[ord_chr_s] += 1
            freq_arr_2[ord_chr_t] += 1

        return (freq_arr_1 == freq_arr_2)