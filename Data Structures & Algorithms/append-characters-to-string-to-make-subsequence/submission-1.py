class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i,j = 0,0
        while i<len(s) and j<len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                i += 1
        if j == 0:
            return len(t)
        if j == len(t):
            return 0
        ans = len(t) - j
        return ans