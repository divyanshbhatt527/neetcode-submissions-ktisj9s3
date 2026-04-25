class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for word in strs:
            w = ''.join(sorted(word))
            if w not in d:
                d[w] = []
                d[w].append(word)
            else:
                d[w].append(word)

        return list(d.values())

        