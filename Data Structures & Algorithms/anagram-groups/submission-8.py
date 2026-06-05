class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        res = []
        for string in strs:
            freq = [0]*26
            for chr in string:
                chr_val = ord(chr) - ord('a')
                freq[chr_val] += 1
            
            if tuple(freq) in hashmap:
                hashmap[tuple(freq)].append(string)
            else:
                hashmap[tuple(freq)] = [string]

        for k,v in hashmap.items():
            res.append(v)

        return res
