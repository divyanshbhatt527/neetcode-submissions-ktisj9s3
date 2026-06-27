class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            length = len(string)
            res += str(length) + "#" + string
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        n = len(s)
        while i < n:
            length = ""
            while i<n and s[i] != "#":
                length += s[i]
                i += 1
            j = i+1
            word = ""
            while j < (int(length)+i+1) and j < n:
                word += s[j]
                j += 1
            print(word)
            res.append(word) 
            i = j
        return res