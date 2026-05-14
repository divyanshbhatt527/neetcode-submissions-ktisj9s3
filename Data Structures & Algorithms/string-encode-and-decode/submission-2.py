class Solution:

    def encode(self, strs: List[str]) -> str:
        res_str = ""
        for word in strs:
            l = len(word)
            res_str += str(l)+'#'+word
        return res_str

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            l = ''
            j = i
            while j < len(s) and s[j]!='#':
                l += s[j]
                j += 1
            word = ''
            i = j+1
            while i < int(l)+j+1:
                word += s[i]
                i += 1
            res.append(word)
        return res

