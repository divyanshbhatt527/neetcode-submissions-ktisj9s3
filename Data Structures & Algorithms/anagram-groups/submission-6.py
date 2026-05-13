class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for word in strs:
            chr_count = [0]*26
            for chr in word:
                index = ord(chr) - ord('a')
                chr_count[index] += 1
            chr_count = tuple(chr_count)
            if chr_count not in hashmap:
                hashmap[chr_count] = [word]
            else:
                hashmap[chr_count].append(word)

        return list(hashmap.values())
        