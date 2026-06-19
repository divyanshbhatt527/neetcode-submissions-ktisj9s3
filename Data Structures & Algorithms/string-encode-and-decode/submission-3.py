class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            l = len(string)
            res += str(l) + "#" + string
            # print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            length = ""
            while s[i] != "#":
                length += s[i]
                i += 1
            print(length)
            j = i + 1
            l = int(length) + i 
            word = ""
            # 5 # h e l l o 5 # w o  r l   d
            # 0 1 2 3 4 5 6 7 8 9 10 11 12 13
            while i < len(s) and j < l+1:
                word += s[j]
                j += 1
            print(word)
            res.append(word)
            i = j 
        return res 