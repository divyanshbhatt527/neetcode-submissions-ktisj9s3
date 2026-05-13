class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        freq_list_s = [0]*26
        freq_list_t = [0]*26

        for i in range(len(s)):
            index_s = ord(s[i])-ord('a')
            index_t = ord(t[i])-ord('a')
            freq_list_s[index_s] += 1
            freq_list_t[index_t] += 1 

        if freq_list_s == freq_list_t:
            return True
        else:
            return False