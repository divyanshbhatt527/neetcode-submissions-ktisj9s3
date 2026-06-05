class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_1 = [0]*26
        freq_2 = [0]*26

        if len(s)!=len(t):
            return False
        
        for i in range(len(s)):
            chr_val1 = ord(s[i]) - ord('a')
            chr_val2 = ord(t[i]) - ord('a')

            freq_1[chr_val1] += 1
            freq_2[chr_val2] += 1

        if freq_1 == freq_2:
            return True
        else:
            return False 