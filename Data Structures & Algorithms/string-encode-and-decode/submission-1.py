class Solution:

    def encode(self, strs: List[str]) -> str:
        # idea: keep length and special char as prefix acting as
        # saperating delimeter
        # eg: output-> 5#Hello5#World

        res_str = []

        for string in strs:
            res_str.append(str(len(string))+'#'+string)

        return ''.join(res_str)


    def decode(self, s: str) -> List[str]:
        # treat the numbers (in form of str) present before '#' 
        # as length and iterate over it and collect the strings 
        # saperately
        result = []
        i = 0
        while i < len(s):
            # find '#'
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            word = s[j+1:j+1+length]
            result.append(word)
            i = j+1+length

        return result


