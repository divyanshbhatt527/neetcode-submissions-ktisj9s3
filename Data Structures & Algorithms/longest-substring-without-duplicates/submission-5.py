class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<=1:
            return len(s)
        max_len = 0
        i,j = 0,0
        char_set = set()
        length = 0
        while i<len(s) and j<len(s):
            if s[j] not in char_set:
                char_set.add(s[j])
                length += 1
                j += 1
            else:
                length = 0
                char_set = set()
                i += 1
                j = i 
            max_len = max(length, max_len)
                

        return max_len