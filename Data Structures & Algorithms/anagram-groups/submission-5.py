class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for word in strs:
            sort_word = tuple(sorted(word))

            if sort_word not in hashmap:
                hashmap[sort_word] = [word]
            else:
                hashmap[sort_word].append(word)

        return list(hashmap.values())
        