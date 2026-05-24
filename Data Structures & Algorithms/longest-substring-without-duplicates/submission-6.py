class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<=1:
            return len(s)
        max_len = 0
        for i in range(len(s)):
            char_set = set()
            for j in range(i,len(s)):
                if s[j] not in char_set:
                    char_set.add(s[j])
                else:
                    break
            max_len = max(max_len,len(char_set))
            
                

        return max_len