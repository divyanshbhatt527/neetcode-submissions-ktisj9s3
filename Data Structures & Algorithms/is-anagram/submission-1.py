class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1 = len(s)
        l2 = len(t)
        if l1!=l2:
            return False
        
        sd = {}
        td = {}

        for i in range(0,l1):
            if s[i] in sd:
                sd[s[i]] =+ 1
            else:
                sd[s[i]] = 0
            

        for j in range(0,l1):
            if t[j] in td:
                td[t[j]] =+ 1
            else:
                td[t[j]] = 0

        if sd == td:
            return True
        else:
            return False