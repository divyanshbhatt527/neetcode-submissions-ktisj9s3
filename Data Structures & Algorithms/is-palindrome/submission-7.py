class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) <= 1:
            return True

        s = s.lower()
        i = 0
        j = len(s)-1
        while i < j:
            while i<j and not s[i].isalnum():
                i += 1
            while i<j and not s[j].isalnum():
                j -= 1

            if i<j and s[i] != s[j]:
                return False
            else:
                i += 1
                j -= 1
        return True