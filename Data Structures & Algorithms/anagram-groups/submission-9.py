class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        chr_freq_arr = {}
        for word in strs:
            chr_freq = [0]*26
            for chr in word:
                chr_ord = ord(chr) - ord('a')
                chr_freq[chr_ord] += 1
            chr_freq = tuple(chr_freq)
            if (chr_freq) in chr_freq_arr:
                chr_freq_arr[chr_freq].append(word)
            else:
                chr_freq_arr[chr_freq] = [word]

        return [item for item in chr_freq_arr.values()]
